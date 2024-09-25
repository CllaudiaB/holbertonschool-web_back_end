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
        """Returns the Base64 part of the Authorization
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
        """Returns the decoded value of a Base64
           string base64_authorization_header"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            valid = base64.b64decode(
                base64_authorization_header, validate=True
            )
        except binascii.Error:
            return None
        return valid.decode("utf-8")
