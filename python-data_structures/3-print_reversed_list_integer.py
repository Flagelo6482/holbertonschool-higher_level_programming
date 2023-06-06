#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    longitud = len(my_list) - 1

    while longitud >= 0:
        print("{:d}".format(my_list[longitud]))
        longitud -= 1
