from flask import Flask, render_template, request, redirect, url_for, abort
from data.json_file_handler import read_json, write_json
app = Flask(__name__)



@app.route('/')
def index():
    # add code here to fetch the job posts from a file
    blog_posts = read_json()
    return render_template('index.html', posts=blog_posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        blog_posts = read_json()
        total_posts = len(blog_posts)
        post_obj = {'id': total_posts + 1,
                    'title': request.form['title'],
                    'content': request.form['content']
                   }
        blog_posts.append(post_obj)
        write_json(blog_posts)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:post_id>')
def delete(post_id):
    blog_posts = read_json()
    for post in blog_posts:
        if post['id'] == post_id:
            blog_posts.remove(post)
            write_json(blog_posts)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    edit_post_obj = None
    blog_posts = read_json()
    for post in blog_posts:
        if post['id'] == post_id:
            edit_post_obj = post
            if request.method == 'POST':
                author = request.form['author']
                title = request.form['title']
                content = request.form['content']
                post['author'] = author
                post['title'] = title
                post['content'] = content
                write_json(blog_posts)
                return redirect(url_for('index'))
            else:
                return render_template('update.html', eidt_post_obj=edit_post_obj)
    if edit_post_obj is None:
        return abort(404)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)