#!/usr/bin/env python3
"""
Authentication file
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ hashing method """
    byts = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(byts, salt)
