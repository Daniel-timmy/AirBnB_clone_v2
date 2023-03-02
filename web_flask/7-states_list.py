#!/usr/bin/python3
"""Starts a flask web application"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page"""
    from models.state import State
    list_state = storage.all(State).values()
    list_state = sorted(list_state, key=lambda k: k.name)
    render_template('7-states_list.html', list_state=list_state)


@app.teardown_appcontext
def app_shutdown():
    """closes the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
