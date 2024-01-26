#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)
"""Flask instance"""


@app.route('/', strict_slashes=False)
"""define route with strict_slashes option"""
def hello_hbnb():
    """define method"""
    return "Hello HBNB!"
"""return value"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    """application listening port""
