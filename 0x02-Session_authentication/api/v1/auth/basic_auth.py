#!/usr/bin/env python3
""" Basic Authentication class """
from api.v1.auth.auth import Auth
import base64
import re
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth inherent from Auth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ encode using base64
        """
        if authorization_header is None\
                or not isinstance(authorization_header, str):
            return None
        if authorization_header.split(' ')[0] != 'Basic':
            return None
        spn = re.search(r'(?<=Basic ).*', authorization_header).span()
        return authorization_header[spn[0]: spn[1]]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """ decode a header using base64
        """
        if base64_authorization_header is None\
                or not isinstance(base64_authorization_header, str):
            return None
        try:
            data = base64_authorization_header.encode('utf-8')

            dcd_data = base64.b64decode(data).decode('utf-8')
            return dcd_data
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """ User Credentials """
        if decoded_base64_authorization_header is None\
                or not isinstance(decoded_base64_authorization_header,
                                  str):
            return (None, None)
        chk = ":" in decoded_base64_authorization_header
        if chk:
            res = decoded_base64_authorization_header.split(":")
            return (res[0], res[1])
        return (None, None)

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """Retrieves a user based on the user's authentication credentials.
        """
        if type(user_email) == str and type(user_pwd) == str:
            try:
                users = User.search({'email': user_email})
            except Exception:
                return None
            if len(users) <= 0:
                return None
            if users[0].is_valid_password(user_pwd):
                return users[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the user from a request.
        """
        auth_header = self.authorization_header(request)
        b64_auth_token = self.extract_base64_authorization_header(auth_header)
        auth_token = self.decode_base64_authorization_header(b64_auth_token)
        email, password = self.extract_user_credentials(auth_token)
        return self.user_object_from_credentials(email, password)
