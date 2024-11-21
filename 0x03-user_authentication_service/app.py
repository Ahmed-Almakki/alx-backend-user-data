#!/usr/bin/env python3
""" flask app"""
from auth import Auth
import flask
from flask import Flask, request, make_response, Response


AUTH = Auth()
app = Flask(__name__)


@app.route("/")
def hello():
    return flask.jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'])
def users():
    """ user post method"""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return flask.jsonify({"email": email,
                              "message": "user created"})
    except Exception:
        return flask.jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'])
def login() -> Union[Response, None]:
    """ login to session"""
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = make_response()
        response.set_cookie('session_id', session_id)
        return flask.jsonify({"email": email, "message": "logged in"})
    return flask.abort(401)


@app.route("/sessions", methods=['DELETE'])
def logout():
    """ logout from session"""
    session_id = request.cookies.get("session_id")
    if session_id in None:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if user is not None:
        AUTH.destroy_session(user.id)
        return flask.redirect("/")
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
