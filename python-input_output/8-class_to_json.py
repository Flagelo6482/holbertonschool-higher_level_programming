#!/usr/bin/python3


"""Class to JSON"""


import json


def class_to_json(obj):
    """
    Function that returns the dictionary
    description with simple data structure
    """
    return obj.__dict__
