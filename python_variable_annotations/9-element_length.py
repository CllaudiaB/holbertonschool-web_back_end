#!/usr/bin/env python3
"""Type an iterable object"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Anotate function's parameters
    and return values with the appropriate type"""
    return [(i, len(i)) for i in lst]
