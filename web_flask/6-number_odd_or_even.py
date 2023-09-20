#!/usr/bin/python3
"""
A Flask web application with multiple routes and
dynamic URL handling, including template rendering
"""

from flask import Flask, render_template

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
    """a simple dynamic route handling on my web application"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text="is cool"):
    """a simple dynamic route with optional parameter"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def is_number(n):
    """a dynamic route that checks for number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """Renders a template using `n`"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Renders a template using `n`"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
