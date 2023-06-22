#!/usr/bin/python3


"""Full rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""
    def __init__(self, width, height):
        """
        Attribute initialization method

        Args:
            width(int) : width
            height(int): height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string readable by the end user
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
