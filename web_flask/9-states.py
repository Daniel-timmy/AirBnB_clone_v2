#!/usr/bin/python3
"""Starts a flask web application"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def cities_and_states(id=None):
    """load all cities of a state"""
    from models.state import State
    a_state = None
    states_list = storage.all(State).values()
    for state in states_list:
        if id == state.id:
            a_state = state
    render_template('9-states.html', states_list=states_list, a_state=a_state)


@app.teardown_appcontext
def app_shutdown():
    """remove current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
