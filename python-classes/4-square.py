#!/usr/bin/python3


"""Access and update private attribute!"""


class Square:
    """Initializing attributes!"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """Property to retun a private attribute"""
    @property
    def size(self):
        return self.__size

    """Property to update a private value"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """Function that returns the area of the square!"""
    def area(self):
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        else:
            return self.__size * self.__size
