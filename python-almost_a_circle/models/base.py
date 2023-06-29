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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method that writes a JSON representation to a file
        Args:
            list_objs(list) :Instance list
        """
        file_name = f"{cls.__name__}.json"

        if list_objs is None or len(list_objs) == 0:
            with open(file_name, mode="w") as file:
                file.write("[]")
        else:
            list_a = []

            for i in list_objs:
                d = {"y": 0, "x": 0, "id": 0, "width": 0, "height": 0}
                d["height"] = i.height
                d["width"] = i.width
                d["id"] = i.id
                d["x"] = i.x
                d["y"] = i.y
                list_a.append(d)

            with open(file_name, mode="w") as file:
                j_son = cls.to_json_string(list_a)
                file.write(j_son)
