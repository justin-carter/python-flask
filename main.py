from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!!!'

@app.route('/hello/<name>')
def show_user_profile(name):
    # show the user profile for that user
    return 'Hello, %s!' % escape(name)

@app.route('/test1')
def test():
    return 'Hello, test!!!'

with app.test_request_context():
    print(url_for('show_user_profile', name='Justin'))