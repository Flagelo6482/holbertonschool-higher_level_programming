#!/usr/bin/python3


"""Append to a file"""


def append_write(filename="", text=""):
    """Function that adds a string to the end of the file"""
    with open(filename, mode="a", encoding="utf-8") as file:
        """
        Args:
            filename(file)  :File text
            mode(mode)      :Openning mode
            encoding(coding):Encoding mode
        """
        return file.write(text)
