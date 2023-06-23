#!/usr/bin/python3


"""Square #1"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """First Square"""
    def __init__(self, size):
        """
        Attribute initialization method

        Args:
            size(int) : size
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Returns a user-readable string"""
        return f"[Rectangle] {self.__size}/{self.__size}"
