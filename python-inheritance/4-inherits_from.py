#!/usr/bin/python3


"""Only subclass of"""


def inherits_from(obj, a_class):
    """
    Function that determines if an object inherits
    (directly or indirectly) from a class
    """
    if a_class in type(obj).__mro__[1:]:
        return True
    else:
        return False
