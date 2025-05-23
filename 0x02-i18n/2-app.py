#!/usr/bin/env python3
"""Basic Flask app with Babel for internationalization."""
from flask_babel import Babel
from flask import Flask, request


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """return locale"""
    return request.accept_languages.best_match(["en", "fr"])
