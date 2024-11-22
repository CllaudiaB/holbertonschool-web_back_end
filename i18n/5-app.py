#!/usr/bin/env python3
"""Basic Flask app"""


from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    "Config languages and timezone"
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


def get_locale():
    """Determine the best match with our supported languages"""
    requested_locale = request.args.get("locale")

    if requested_locale in app.config["LANGUAGES"]:
        return requested_locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user(id: int):
    user = users[id]
    return(user)


@app.before_request
def before_request():
    user = request.args.get("login_as")
    if user:
        g.user = get_user(int(user))
    return None


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def home():
    """Return the content of the 5-index.html file"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()
