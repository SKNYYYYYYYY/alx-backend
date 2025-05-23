#!/usr/bin/env python3
"""
This module initializes a basic Flask web application with Babel integration.
It supports internationalization (i18n) by selecting between English and French
based on the user's browser language preferences.
"""

from flask import Flask, request, render_template
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for supported languages ('en' and 'fr')
    based on the client's request headers.
    """
    return request.accept_languages.best_match(["en", "fr"])

@app.route("/")
def index() -> str:
    """
    Render the index HTML template with translated content.
    """
    return render_template("3-index.html")

if __name__ == "__main__":
    app.run()
