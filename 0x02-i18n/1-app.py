#!/usr/bin/env python3
"""sets babel defaults"""
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """default configurations"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
conf = Config()
app.config.from_object(conf)
babel = Babel(app)


@app.route("/")
def index():
    """renders html file"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
