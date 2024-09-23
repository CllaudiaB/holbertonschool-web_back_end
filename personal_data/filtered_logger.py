#!/usr/bin/env python3
import re
from typing import List


def filter_datum(fields: List[str], redaction: str , message: str, separator: str) -> str:
    parts = message.split(separator)
    for idx, text in enumerate(parts):
        if text.startswith(tuple(fields)):
            parts[idx] = re.sub(r"(=)(.*)", rf"\1{redaction}", text)
    return separator.join(parts)
