#!/usr/bin/python3
"""
Print Square
"""


def print_square(size):
    """Square print!"""
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
