from flask import Flask, render_template
from markupsafe import escape # escape prevents injection, eg wont allow: <script>alert("bad")</script>

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/projects/')#like folders
def projects():
    return 'The project page'

@app.route('/about')#like file
def about():
    return 'The about page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hollo.html', name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
