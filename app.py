from flask import Flask, render_template
from data.json_file_handler import read_json
app = Flask(__name__)



@app.route('/')
def index():
    # add code here to fetch the job posts from a file
    blog_posts = read_json()
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)