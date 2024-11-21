#!/usr/bin/env python3
""" flask app"""
from auth import Auth
import flask
from flask import Flask, request


AUTH = Auth()
app = Flask(__name__)


@app.route("/")
def hello():
    return flask.jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'])
def users():
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return flask.jsonify({"email": email,
                              "message": "user created"})
    except Exception:
        return flask.jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")