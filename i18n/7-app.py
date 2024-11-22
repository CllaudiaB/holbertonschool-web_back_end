#!/usr/bin/env python3
"""Basic Flask app"""


from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

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

    if g.user:
        locale = g.user.get("locale")
        if locale in app.config["LANGUAGES"]:
            return g.user.get("locale")

    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_timezone():
    """Define timezone"""
    tz = request.args.get("timezone")
    if tz:
        try:
            timezone = pytz.timezone(tz)
            return timezone.zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user:
        tz = g.user.get("timezone")
        try:
            timezone = pytz.timezone(tz)
            return timezone.zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user(id):
    """Returns a user dictionary"""
    if id:
        id = int(id)
    return users.get(id, None)


@app.before_request
def before_request():
    """Find a user"""
    user = request.args.get("login_as")
    g.user = get_user(user)


babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route("/")
def home():
    """Return the content of the 7-index.html file"""
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run()
