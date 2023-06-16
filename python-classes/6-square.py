#!/usr/bin/python3


"""Coordinates of a square!"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    """Property to return a private attribute"""
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

    """Property to return a private attribute"""
    @property
    def position(self):
        return self.__position

    """Property to update a private value"""
    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(value, int) or value <= 0:
                raise TypeError("position must be a tuple of 2 positive\
                                                              integers")
        self.__position = value

    """Function that return the area of the square!"""
    def area(self):
        return self.__size * self.__size

    """Function to print our square!"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
