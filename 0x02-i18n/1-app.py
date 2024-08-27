#!/usr/bin/env python3

""" Doc for app script """

from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ Doc for config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.rouute('/')
def index():
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run(debug=True)
