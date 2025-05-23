#!/usr/bin/env python3
""" babel for intenationalizatopn"""
from flask_babel import Babel
from flask import Flask, render_template, request, g


class Config:
    """default configurations"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
app = Flask(__name__)
conf = Config()
app.config.from_object(conf)
babel = Babel(app)


def get_user():
    """returns a user dictionary"""
    user_id = request.args.get("login_as")
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """get user"""
    g.user = get_user()


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
    return render_template(
        "5-index.html",
        username=g.user['name'] if g.user else "guest")


if __name__ == "__main__":
    app.run()
