#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000
Routes:
    /states_list: display an HTML page
"""

from flask import Flask, render_template, request
from models import storage
from models.state import State

app = Flask(__name__)


from flask import Flask, render_template
from typing import Dict, List

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list() -> str:
    """
    Returns a rendered HTML template with a list of all states.

    :return: A string representing the rendered HTML template.
    """
    states: List[Dict[str, str]] = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
