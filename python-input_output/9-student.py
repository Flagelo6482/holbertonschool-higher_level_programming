#!/usr/bin/python3


"""Student to JSON"""


class Student:
    """Class a student creates"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    """
    Initialization constructor
    Args:
        first_name(string) :First name
        last_name(string)  :Last name
        age(int)           :Age
    """

    def to_json(self):
        """
        Method that retrieves a dictionary
        representation in an instance
        """
        return self.__dict__
