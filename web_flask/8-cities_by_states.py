#!/usr/bin/python3
"""Starts a flask web application"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """load all cities of a state"""
    from models.state import State
    states_list = storage.all(State).values()
    render_template('8-cities_by_states.html', states_list=states_list)


@app.teardown_appcontext
def app_shutdown():
    """remove current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
