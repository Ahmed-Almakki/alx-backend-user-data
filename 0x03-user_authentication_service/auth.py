#!/usr/bin/env python3
"""
Authentication file
"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """ hashing method """
    byts = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(byts, salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ register user in database if not exists"""
        chk = True
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            chk = False
        if chk:
            raise ValueError("User {} already Exists".format(email))
        hased = _hash_password(password)
        user = self._db.add_user(email, hased)
        return user
