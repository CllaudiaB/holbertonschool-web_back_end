#!/usr/bin/env python3
"""Redis exercices"""
import redis
from typing import Any
import uuid


class Cache:
    """Cache"""
    def __init__(self):
        """Init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """Store data in Redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
