# -*- coding: iso-8859-15 -*-

import sys

from flask import Flask

app = Flask(__name__)


## Devolver una p�gina estatica

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


@app.route('/home', methods=['GET'])
def home():
    return app.send_static_file('home.html')


@app.route('/login', methods=['GET'])
def login():
    return app.send_static_file('login.html')


@app.route('/signup', methods=['GET'])
def signup():
    return app.send_static_file('signup.html')


## Devolver de manera dinamica

@app.route('/ex1')
def function_for_ex1():
    """
    It processes the '/ex1' url.
    :return: basic HTML
    """
    return "Content of the url /ex1"


@app.route('/ex2')
def function_for_ex2():
    """
    It process the '/' url.
    :return: basic HTML for /ex2
    """
    return '<!DOCTYPE html> ' \
           '<html lang="es">' \
           '<head>' \
           '<title> This is the page title </title>' \
           '</head>' \
           '<body> <div id ="container">' \
           '<h1>Example of HTML Content</h1>' \
           'Return to the homepage by clicking <a href="/"> here</a> </html>' \
           '</html>'


# start the server with the 'run()' method
if __name__ == '__main__':
    if sys.platform == 'darwin':  # different port if running on MacOsX
        app.run(debug=True, port=8080)
    else:
        app.run(debug=True, port=80)
