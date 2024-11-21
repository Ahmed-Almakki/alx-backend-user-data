#!/usr/bin/env python3
""" flask app"""
from auth import Auth
import flask
from flask import Flask, request, make_response


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


@app.route("/sessions", methods=['POST'])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        out = "session_id=" + str(session_id)
        response = make_response(out)
        response.set_cookie('session_id', session_id)
        return flask.jsonify({"email": email, "message": "logged in"})
    flask.abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
