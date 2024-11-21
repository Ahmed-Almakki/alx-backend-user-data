#!/usr/bin/env python3
""" flask app"""
import flask
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return flask.jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
