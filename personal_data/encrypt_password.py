#!/usr/bin/env python3
"""Encrypting passwords"""

import bcrypt
from typing import ByteString


def hash_password(password: str) -> ByteString:
    """Return hashed password"""
    return bcrypt.hashpw(password, bcrypt.gensalt())
