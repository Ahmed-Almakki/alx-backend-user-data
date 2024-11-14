#!/usr/bin/env python3
"""class SessionAuth that inherits from Auth"""
from api.v1.auth.auth import Auth
from typing import List, TypeVar


class SessionAuth(Auth):
    """ Session object used for authentication"""
