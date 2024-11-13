#!/usr/bin/env python3
""" Basic Authentication class """
from api.v1.auth.auth import Auth
import base64
import re


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
