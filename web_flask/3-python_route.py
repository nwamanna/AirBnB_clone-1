#!/usr/bin/python3
"""Starts a Flask web application that listens on 0.0.0.0, port 5000.
    Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): display “Python ”, followed by the value of the text
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ displays hello world """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ display “C ” followed by the value of the text variable """
    space_text = text.replace('_', ' ')
    return "C {}".format(space_text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ display “Python ”, followed by the value
        of the text variable (replace underscore _
        symbols with a space
    """
    space_text = text.replace('_', ' ')
    return "Python {}".format(space_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
