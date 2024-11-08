#!/usr/bin/env python3
""" Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """User passwords should NEVER be stored in plain text in a db"""
    pas = str.encode(password)
    hashed = bcrypt.hashpw(pas, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Implement an is_valid function that expects 2 argument"""
    pas = str.encode(password)
    if bcrypt.checkpw(pas, hashed_password):
        return True
    else:
        return False
