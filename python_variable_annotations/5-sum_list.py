#!/usr/bin/env python3
"""Complex types - list of floats"""

from math import sum
from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes a list input_list of floats as argument
    and returns their sum as a float"""
    return sum(float(number) for number in input_list)
