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
        return False

    def authorization_header(self, request=None) -> str:
        """ autherization header
        Return:
            request: it well be Flask request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ puplic method curent user
        Return:
             request
        """
        return None
