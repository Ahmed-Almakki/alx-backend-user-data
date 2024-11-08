#!/usr/bin/env python3
""" Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """User passwords should NEVER be stored in plain text in a db"""
    pas = str.encode(password)
    hashed = bcrypt.hashpw(pas, bcrypt.gensalt())
    return hashed
