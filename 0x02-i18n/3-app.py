#!/usr/bin/env python3
"""The imported module"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """The class defintion"""
    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """the get definition"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """the index defintion"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()