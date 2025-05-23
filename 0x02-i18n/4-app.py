#!/usr/bin/env python3
""" babel for intenationalizatopn"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """default configurations"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
conf = Config()
app.config.from_object(conf)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """get locale"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """renders html file"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
