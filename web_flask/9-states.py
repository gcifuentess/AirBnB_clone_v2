#!/usr/bin/python3
'''Flask Module AirBnB_Clone_v2'''
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states', defaults={"state_id": "No_ID"},
           strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id):
    if state_id == "No_ID":
        states = storage.all(State).values()
        default = 0
    else:
        try:
            states = storage.all(State)['State.' + state_id]
            default = 1
        except:
            states = None
            default = 2
    return render_template('9-states.html', states=states, default=default)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
