#!/usr/bin/env python3
"""module for flask app and babel"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configuration class for Flask application."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """determijes tge locale to use"""
    locale = request.args.get("locale")
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def hello():
    """renders 0-index.html"""
    return render_template("1-index.html")
