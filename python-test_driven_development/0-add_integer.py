#!/usr/bin/python3
"""
Sum arithmetic

Function
"""


def add_integer(a, b=98):
    """
    Function that returns the sum of two numbers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
