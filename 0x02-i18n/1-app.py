#!/usr/bin/env python3
"""sets babel defaults"""
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    LANGUAGES = ["en", "fr"]
    default_locale = "en"
    default_timezone = "UTC"


app = Flask(__name__)
conf = Config()
app.config.from_object(conf)
babel = Babel(app)

# render_template("1-index.html")

if __name__ == "__main__":
    app.run()
