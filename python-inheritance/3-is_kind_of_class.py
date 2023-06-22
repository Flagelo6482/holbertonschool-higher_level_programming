#!/usr/bin/python3


"""
Same class
or inherit
from
"""


def is_kind_of_class(obj, a_class):
    """
    Function that returns "true"
    if the object is an instance or instance
    of the class that I here, else "False"
    """
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
