#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
from models.state import State
from os import getenv

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """Displays a HTML page with a list of all states"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda x: x.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """Displays a HTML page with the cities of a specific state"""
    states = storage.all(State).values()
    state = None
    for s in states:
        if s.id == id:
            state = s
            break
    if state:
        cities = state.cities if getenv('HBNB_TYPE_STORAGE') == 'db' \
            else state.cities()
        cities = sorted(cities, key=lambda x: x.name)
        return render_template('9-state.html', state=state, cities=cities)
    else:
        return render_template('9-not_found.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
