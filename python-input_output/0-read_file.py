#!/usr/bin/python3


"""
Read file
"""


def read_file(filename=""):
    """Function to read a file and print it"""
    with open(filename, mode="r", encoding="utf-8") as file:
        """
        Args:
            filename(file)  :File text
            mode(mode)      :Opening mode
            encoding(string):Coding
        """
        var = file.read()
        print(var, end="")
