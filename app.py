#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
app = Flask(__name__)
from myapp import views

app.add_url_rule('/', 'index', views.index)
app.add_url_rule('/hello/', 'hello_world', views.hello_world)
app.add_url_rule('/<username>/<surname>/', 'user', views.show_user_profile)





# @app.route('/') We then use the route() decorator to tell Flask what URL should trigger(call) our function.


"""
@app.route('/user/<username>/<surname>')
def show_user_profile(username, surname):
    # show the user profile for that user
    return 'User name {}, User surname {}'.format(username, surname)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    if post_id == 123:
        return "<h1>1234</h1>"
    else:
        return 'Post %d' % post_id

"""