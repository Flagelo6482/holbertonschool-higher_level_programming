#!/usr/bin/python3


"""Save Object to a file"""


import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        """
        Args:
            filename(file)   :File text
            mode(mode)       :Openning mode
            encoding(coding) :Encoding
        """
        file.write(json.dumps(my_obj))
        file.write("\n")
