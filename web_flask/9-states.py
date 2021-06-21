#!/usr/bin/python3
"""Create Flask for State objects"""
from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template
STATES = Flask(__name__)
STATES.url_map.strict_slashes = False


@STATES.route('/states/')
@STATES.route('/states/<id>')
def states_and_cities(id=0):
    new_dict = {}
    # store all States in an object
    state_dict = storage.all(State)
    # sort the dictionary by key/value pairs
    for state in state_dict.values():
        if str(id) == state.id:
        # add state match to new_dict
            new_dict['name'] = state.name
            new_dict['id'] = state.id
            break
    if new_dict:
        # repeat process for City
        city_dict = storage.all(City)
        sorted_city = sorted(city_dict.values(), key=lambda x: x.name)
        return render_template('9-states.html', States=new_dict,
                               Cities=sorted_city, signal=0)
    if id == 0:
        sorted_dict = sorted(state_dict.values(), key=lambda x: x.name)
        return render_template('9-states.html', States=sorted_dict,
                               city=None, signal=1)

    else:
       return render_template('9-states.html', state=None, city=None,
                              signal=2)


@STATES.teardown_appcontext
def tear_down(error):
    if storage:
        storage.close()

if __name__ == '__main__':
    STATES.run(debug=True, host='0.0.0.0', port=5000)
