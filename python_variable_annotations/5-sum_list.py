#!/usr/bin/env python3
"""Complex types - list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes a list input_list of floats as argument
    and returns their sum as a float"""
    sum = 0

    for number in input_list:
        sum += number

    return sum
