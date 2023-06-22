#!/usr/bin/python3


"""Integer validator"""


class BaseGeometry:
    """Class with two methods that generate a raise"""
    def area(self):
        """
        Function that generates a raise error

        Raise:
            Exception:
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function that checks an integer

        Args:
            name(string): name
            value(int)  : integer
        Raise:
            TypeError: <name> must be an integer
            ValueError: <name> must be be greater than 0
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
