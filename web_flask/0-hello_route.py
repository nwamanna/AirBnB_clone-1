#!/usr/bin/python3
""" /: display “Hello HBNB! """
from web_flask import app

@app.route('/', strict_slashes=False)
def hello_world():
    """ displays hello world """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
