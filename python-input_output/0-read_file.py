#!/usr/bin/python3


"""
Read file
"""


def read_file(filename=""):
    """Function to read a file and print it"""
    with open(filename, encoding='utf-8') as file:
        var = file.read()
        print(var)
