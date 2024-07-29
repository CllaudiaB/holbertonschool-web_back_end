#!/usr/bin/env python3
"""Complex types - list of floats"""


def sum_list(input_list: "list[float]") -> float:
    """takes a list input_list of floats as argument
    and returns their sum as a float"""
    sum: float = None
    for number in input_list:
        sum += number

    return sum
