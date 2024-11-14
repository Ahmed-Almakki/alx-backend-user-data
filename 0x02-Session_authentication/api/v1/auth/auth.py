#!/usr/bin/env python3
""" class to manage the API authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Authenticatin class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ a puplic method that require authentication
        Return:
            path: path of the
            excluded_paths: deleted paths
        """
        check = path
        if path is None or excluded_paths is None\
                or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            check = path + "/"
        if path in excluded_paths or check in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ autherization header
        Return:
            request: it well be Flask request
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ puplic method curent user
        Return:
             request
        """
        return None
