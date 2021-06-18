#!/usr/bin/python3
"""Create Flask for State objects"""
from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template
STATES = Flask(__name__)
STATES.url_map.strict_slashes = False


@STATES.route('/cities_by_states')
def cities_list():
    # store all States in an object
    state_dict = storage.all(State)
    # sort the dictionary by key/value pairs
    sorted_dict = sorted(state_dict.values(), key=lambda x: x.name)
    # repeat process for City
    city_dict = storage.all(City)
    sorted_city = sorted(city_dict.values(), key=lambda x: x.name)
    return render_template('7-states_list.html', States=sorted_dict,
                           Cities=sorted_city)


@STATES.teardown_appcontext
def tear_down(error):
    if storage:
        storage.close()

if __name__ == '__main__':
    STATES.run(debug=True, host='0.0.0.0', port=5000)
