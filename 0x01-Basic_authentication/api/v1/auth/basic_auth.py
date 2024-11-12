#!/usr/bin/env python3
""" Basic Authentication class """
from api.v1.auth.auth import Auth
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
