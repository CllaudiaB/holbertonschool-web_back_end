#!/usr/bin/env python3
"""Basic auth"""

import base64
import binascii
import re
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic auth"""

    def extract_base64_authorization_header(
            self, authorization_header: str
    ) -> str:
        """Return the Base64 part of the Authorization
            header for a Basic Authentication"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return
        value = re.search(r"[^\s]*$", authorization_header)
        return value.group()

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Return the decoded value of a Base64
           string base64_authorization_header"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            valid = base64.b64decode(
                base64_authorization_header, validate=True
                )
            if valid:
                return valid.decode("utf-8")
        except binascii.Error:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """Return the user email and password
           from the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" in decoded_base64_authorization_header:
            res = decoded_base64_authorization_header.split(":")
            return tuple(res)
        else:
            return None, None
