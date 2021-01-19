#!/usr/bin/python3
'''Working with Flask Module'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def show_post(text):
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', defaults={"text": "is cool"},
           strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def show_post_python(text):
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
