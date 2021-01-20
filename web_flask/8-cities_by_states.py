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
    states_dict = storage.all(State)
    states = objs_dict(states_dict)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    from flask import render_template
    from models.state import State
    states_dict = storage.all(State)
    states = objs_dict(states_dict)
    state_cities = {}
    for state in states_dict.values():
        cities = objs_dict(list(state.cities))
        state_cities[state.id] = cities
    return render_template('8-cities_by_states.html',
                           states=states, cities=state_cities)


def objs_dict(cls_dict_list):
    '''returns a dictionary with the name/id key/value
    of the objs in a class dict'''
    obj_dict = {}
    if type(cls_dict_list) is dict:
        for obj in cls_dict_list.values():
            obj_dict[obj.name] = obj.id
    elif type(cls_dict_list) is list:
        for obj in cls_dict_list:
            obj_dict[obj.name] = obj.id
    return obj_dict


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
