#!/usr/bin/python3


"""Create object from a JSON file"""


import json


def load_from_json_file(filename):
    """Function that creates an object from a "JSON file"""
    with open(filename, mode="r", encoding="utf-8") as file:
        """
        Args:
            filename(file)   :File text
            mode(mode)       :Openning mode
            encoding(coding) :Encoding
        """
        return json.loads(file.read())
