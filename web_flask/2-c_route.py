#!/usr/bin/python3
""" This module builds a script that starts a Flask app"""
# web application must be listening on 0.0.0.0
# port must be set to 5000
# Routes: / : display "Hello HBNB!"
# must use the option strict_slashes=False in route definition

from flask import Flask
HBNB = Flask(__name__)
HBNB.url_map.strict_slashes = False


@HBNB.route('/')
def hello():
    """hello is route definition for '/'"""
    return 'Hello HBNB!'


@HBNB.route('/hbnb')
def hello2():
    """hello2 is route definition for '/hbnb'"""
    return 'HBNB'


@HBNB.route('/c/<text>')
def text_variable(text):
    # read instructions!!! use replace() built-in
    return 'C %s' % text.replace("_", " ")

if __name__ == '__main__':
    HBNB.run(debug=True, host='0.0.0.0', port=5000)