#!/usr/bin/python3


"""My list sorted!"""


class MyList(list):
    """Print the list but sorted"""
    def print_sorted(self):
        print(sorted(self))
