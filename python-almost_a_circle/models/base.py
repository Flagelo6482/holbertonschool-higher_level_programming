#!/usr/bin/python3


"""Base class"""


import json
import os


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
        list_a = []

        if list_objs is None or len(list_objs) == 0:
            with open(file_name, mode="w") as file:
                file.write(cls.to_json_string(list_a))
        else:
            for i in list_objs:
                list_a.append(i.to_dictionary())
            with open(file_name, mode="w") as file:
                file.write(cls.to_json_string(list_a))

    @staticmethod
    def from_json_string(json_string):
        """
        That returns the list of the JSON string representation
        Args:
            json_string(dict): Dictionary
        """
        if json_string is None:
            return list()
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Class method, which creates a dummy instance and returns it
        Args:
            cls(class)       :Class
            dictionary(dict) :Arguments
        """
        inst = cls(**dictionary)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """
        Function that returns a list of instances
        """
        file_name = f"{cls.__name__}.json"
        list_inst = []

        if not os.path.exists(file_name):
            return list_inst

        with open(file_name, mode="r") as file:
            json_data = file.read()
        dictionaries = cls.from_json_string(json_data)

        for dict in dictionaries:
            inst = cls.create(**dict)
            list_inst.append(inst)

        return list_inst
