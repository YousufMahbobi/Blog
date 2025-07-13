from flask import Flask, render_template, request, redirect, url_for
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)