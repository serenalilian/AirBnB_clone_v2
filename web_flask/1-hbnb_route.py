#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)
"""create flask instance"""


@app.route('/', strict_slashes=False)
def hbnb_two():
    """define method"""
    return "Hello HBNB!"

@app.route('/', strict_slashes=False)
def hbnb_three():
    """define method"""
    return "HBNB"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    """app port number"""
