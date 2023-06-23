#!/usr/bin/python3


"""Square #2"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square #2"""
    def __init__(self, size):
        """
        Attribute initialization method

        Args:
            size(int) : size
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """Returns a user-readable string"""
        return f"[Square] {self.__size}/{self.__size}"
