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
        if path is not None and path[-1] != "/":
            path = path + "/"
        if excluded_paths is not None and excluded_paths != []:
            excluded_paths = [i + "/" if i[-1] != "/" else i
                              for i in excluded_paths]
        if path is None or path not in excluded_paths \
                or excluded_paths is None or excluded_paths == []:
            return True
        return False

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
