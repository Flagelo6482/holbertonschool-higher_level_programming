#!/usr/bin/python3


"""Base class"""


import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization constructor

        Args:
            id(int or None) : Int or None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Function that returns a dictionary in a JSON string
        Args:
            list_dictionaries(dict) :Dictionary
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
