#!/usr/bin/python3


"""Student to JSON with filter"""


class Student:
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """
        Attribute constructor method
        Args:
            first_name(string) : First name
            last_name(string)  : Last name
            age(int)           : Age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a
        Student instance
        Args:
            attrs(None or list)
        """
        if attrs is None:
            atr = self.__dict__
        else:
            dic = dict()
            for i in attrs:
                if i in self.__dict__:
                    dic[i] = self.__dict__.get(i)
            atr = dic

        return atr
