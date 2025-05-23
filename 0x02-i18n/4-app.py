#!/usr/bin/env python3
"""Basic Flask app with Babel for internationalization."""
from flask_babel import Babel, gettext
from flask import Flask, request, render_template


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """return locale"""
    params = request.args
    locale = params['locale']
    if locale in ["en", "fr"]:
        return locale
    return request.accept_languages.best_match(["en", "fr"])


@app.route("/")
def index():
    """renders html file"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
