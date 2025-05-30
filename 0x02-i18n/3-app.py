#!/usr/bin/env python3
"""Basic Flask app with Babel for internationalization."""
from flask_babel import Babel, gettext
from flask import Flask, request, render_template


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """return locale"""
    return request.accept_languages.best_match(["en", "fr"])


@app.route("/")
def index():
    """renders html file"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()
