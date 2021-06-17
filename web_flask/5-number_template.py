#!/usr/bin/python3
""" This module builds a script that starts a Flask app"""
# web application must be listening on 0.0.0.0
# port must be set to 5000
# Routes: / : display "Hello HBNB!"
# must use the option strict_slashes=False in route definition

from flask import Flask, render_template
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


@HBNB.route('/python/<string:text>')
# ^^^ defines route with string text as variable
@HBNB.route('/python/')
# ^^^ defines route if no text is supplied
def text_variable2(text='is cool'):
    # defineing a default variable value for string above
    return 'Python %s' % text.replace("_", " ")


@HBNB.route('/number/<int:n>')
def number(n):
    return '%d is a number' % n


@HBNB.route('/number_template/<int:n>')
def is_number_template(n):
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    HBNB.run(debug=True, host='0.0.0.0', port=5000)
