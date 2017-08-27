from flask import render_template

def index():
    return render_template('index.html')

# @app.route('/hello')
def hello_world():
    return render_template('hello world.html')

# @app.route('/user/<username>/<surname>')
def show_user_profile(username, surname):
    return render_template('users.html')