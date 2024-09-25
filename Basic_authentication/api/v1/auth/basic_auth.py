#!/usr/bin/env python3
"""Basic auth"""

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
