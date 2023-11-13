#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000
Routes:
    /states_list: display an HTML page
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)

@app.route("/states", strict_slashes=False)
@app.route("/states/<state_id>", strict_slashes=False)
def states(state_id=None):
    states = storage.all(State).values()
    if state_id:
        for st in states:
            if st.id == state_id:
                states = [st]
                break
    return render_template("9-states.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
