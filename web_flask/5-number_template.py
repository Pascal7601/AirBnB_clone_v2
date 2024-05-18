#!/usr/bin/python3
"""
script that takes in a variable
on the route
"""

from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    displays content at the root folder
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    displays content in the hbnb route
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    navigates to the c section of the
    browser
    """
    new_text = ' '.join(text.split('_'))
    return f"C {escape(new_text)}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_route(text):
    """
    displays content in the python
    section keyed by the user
    """
    if text is None:
        new_text = 'is cool'
    else:
        new_text = ' '.join(text.split('_'))
    return f"Python {escape(new_text)}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "n is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_tag(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
