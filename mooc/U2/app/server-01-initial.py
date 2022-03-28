# -*- coding: iso-8859-15 -*-

import sys

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    """
    It processes the '/' url.
    :return: basic HTML
    """
    return "Hello Word! This is the answer of the server"


# start the server with the 'run()' method
if __name__ == '__main__':
    if sys.platform == 'darwin':  # different port if running on MacOsX
        app.run(debug=True, port=8080)
    else:
        app.run(debug=True, port=80)
