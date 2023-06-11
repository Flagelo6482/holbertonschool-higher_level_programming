#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    longitud = len(my_list) - 1
    for longitud in range(longitud, -1, -1):
        if isinstance(longitud, int):
            print("{:d}".format(my_list[longitud]))
