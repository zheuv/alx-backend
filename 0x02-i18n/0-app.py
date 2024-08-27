#!/usr/bin/env python3
""" Document for the app script """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ Doc for function """
    render_template("templates/index.html")


if __name__ == '__main__':
    app.run(debug=True)
