#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000
Routes:
    /states_list: display an HTML page
"""
import sys
sys.path.append("/home/ryan/source/school/holbertonschool-AirBnB_clone_v2/")

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Returns a rendered HTML template with a list of all states.

    :return: A string representing the rendered HTML template.
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
