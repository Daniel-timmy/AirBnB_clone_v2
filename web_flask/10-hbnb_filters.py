#!/usr/bin/python3
"""Starts a flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """load all City, State, and Amenities"""
    from models.state import State
    from models.amenity import Amenity
    amenities = storage.all(Amenity).values()
    states = storage.all(State).values()
    render_template('10-hbnb_filters.html', amenities=amenities, states=states)


@app.teardown_appcontext
def app_shutdown():
    """remove current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
