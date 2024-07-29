#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""
from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, int | float]:
    """Takes 2 arguments and return a tuple"""
    return k, v
