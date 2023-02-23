#!/usr/bin/python3
"""Starts a flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Return hello HBNB"""
    return "Hello HBNB"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """returns c and some text"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/(<text>)', strict_slashes=False)
def display_python(text="is cool"):
    """returns python and 'text' otherwise python is cool"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<n>', strict_slashes=False)
def display_number(n):
    """displays an integer"""
    if isinstance(n, int):
        return '{} is a number'.format(n)


@app.route('/number/template/<n>', strict_slashes=False)
def number_template(n):
    """display an HTML page only if n is an integer"""
    if isinstance(n, int):
        render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)