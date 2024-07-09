#!/usr/bin/python3
"""
Script starts a Flask web application that displays states and amenities
listed in alphabetical order.
"""

from flask import Flask, render_template
from models import *
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """
    Display web page with a list of all State and Amenity objects.
    
    Retrieves all State and Amenity objects from the storage.
    Passes the lists of states and amenities to the HTML template '10-hbnb_filters
    """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage on teardown.

    This function is called automatically when the application context ends.
    It ensures that the storage is properly closed.
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')