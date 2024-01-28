#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
=======
from flask import Flask


app = Flask(__name__)
"""Flask instance"""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """define method"""
    return "Hello HBNB!"
"""return value"""


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    """application listening port"""
>>>>>>> b1ff1ababf69d0a7061807e934bdc739d87176b1
