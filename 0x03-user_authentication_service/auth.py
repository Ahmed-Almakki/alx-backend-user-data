#!/usr/bin/env python3
"""
Authentication file
"""
import bcrypt
from db import DB
from typing import Union
from user import User
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """ hashing method """
    byts = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(byts, salt)


def _generate_uuid() -> str:
    """ generate unique id"""
    return str(uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """ validate email and password"""
        try:
            user = self._db.find_user_by(email=email)
            password = password.encode('utf-8')
            x = bcrypt.checkpw(password, user.hashed_password)
            if x:
                return True
            return False
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """ creating session and return it't ID"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            user.session_id = session_id
            return session_id
        except Exception as e:
            pass
        return

    def get_user_from_session_id(self, session_id: str) -> Union[None, User]:
        """ get user id session"""
        if session_id:
            return self._db.find_user_by(session_id=session_id)
        return None
