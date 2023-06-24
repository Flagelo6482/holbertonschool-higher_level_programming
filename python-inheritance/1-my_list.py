#!/usr/bin/python3
"""My list sorted!"""


class MyList(list):
    """Clas that prints an ordered list"""

    def print_sorted(self):
        """
        Function that prints
        and ordered list


        """
        print(sorted(self))
