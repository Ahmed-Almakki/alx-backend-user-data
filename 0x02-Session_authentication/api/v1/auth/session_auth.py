#!/usr/bin/env python3
"""class SessionAuth that inherits from Auth"""
from api.v1.auth.auth import Auth
from typing import List, TypeVar
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """ Session object used for authentication"""
