#!/usr/bin/env python3
"""Basic Flask app"""


from flask import Flask, render_template, request
from flask_babel import Babel


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


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def home():
    """Return the content of the 4-index.html file"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
