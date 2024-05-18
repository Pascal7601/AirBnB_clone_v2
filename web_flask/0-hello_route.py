#!/usr/bin/python3
"""
script that starts a flask web app
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """
    function that starts a web flask
    application
    """
    return "Hello HBNB!"
