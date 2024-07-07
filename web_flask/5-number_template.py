#!/usr/bin/python3
"""
Flask web application that displays "Hello HBNB!" at the root route.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Displays 'C followed by the value of the text variable
    (replace underscore _ symbols with space)
    """
    display_text = text.replace('_', ' ')
    return 'C {}'.format(display_text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    Displays 'Python' , followed by the value of the text variable
    (replace underscore _ symbols with a space)
    """
    display_text = text.replace('_', ' ')
    return 'Python {}'.format(display_text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Displays 'n is a number' only if n is an integer
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """Displays a HTML page only if n is an integer"""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
