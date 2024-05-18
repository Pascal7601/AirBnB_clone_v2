#!/usr/bin/python3
"""
a script that starts a web flask app
"""

from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    """
    the home page file
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """
    displays the hbnb page
    """
    return "HBNB"


if  __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
    
