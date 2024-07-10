#!/usr/bin/python3
"""
This script starts a Flask web application to display States
"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/states_lis', strict_slashes=False)
def states_list():
    """Displays an HTML page with the states listed in abc order"""
    return render_template("7-states_list.html",
                           states=storage.all(State))


@app.teardown_appcontext
def teardown(exception):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
