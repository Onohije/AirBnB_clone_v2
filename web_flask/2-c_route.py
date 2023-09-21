#!/usr/bin/python3
"""
A Flask web application with multiple routes and
dynamic URL handling
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """a simple index page for my web application"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """a simple additional route to my web application"""
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    """a simple dynamic url handling on my web application"""
    return "C {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
