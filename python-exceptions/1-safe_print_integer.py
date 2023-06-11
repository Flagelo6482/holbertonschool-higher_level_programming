#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(isinstance(value, int)))
        return True

    except ValueError:
        return False
