#!/usr/bin/python3


"""Area of a square!"""


class Square:
    """Initializing attributes!"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """Function that returns the area of the square!"""
    def area(self):
        return self.__size * self.__size
