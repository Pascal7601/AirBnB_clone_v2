#!/usr/bin/python3
"""
script that takes in a variable
on the route
"""

from flask import Flask
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
