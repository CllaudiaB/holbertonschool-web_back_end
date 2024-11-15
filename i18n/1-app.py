#!/usr/bin/env python3
"""Basic Flask app"""


from flask import Flask, render_template
from flask_babel import Babel


class Config():
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route("/")
def home():
    """Return the content of the 0-index.html file"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
