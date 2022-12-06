
from flask import Flask

app = Flask(__name__)


@app.route('/about')
def about():
    return 'The about page'


@app.route('/blog')
def blog():
    return 'The blog page'


@app.route('/blog/<string: blog_id>')
def blogpost(blog_id):
    return f'This is blog post number {blog_id}'


if __name__ == '__main__':
    app.run(debug=True)
