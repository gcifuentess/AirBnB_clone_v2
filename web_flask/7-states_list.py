#!/usr/bin/python3
'''Flask Module AirBnB_Clone_v2'''
from flask import Flask
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    from flask import render_template
    from models.state import State
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
