#!/usr/bin/env python3
"""Complex types - mixed list"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a list mxd_lst of integers and floats
    and returns their sum as a float"""
    sum = 0

    for number in mxd_lst:
        sum += number

    return sum
