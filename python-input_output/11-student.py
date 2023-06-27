#!/usr/bin/python3


"""Student to disk and reload"""


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

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        Args:
            json(dict): Diccionary
        """
        dic = self.__dict__

        for k, v in json.items():
            if (dic.get(k) == self.first_name):
                self.first_name = v
            elif (dic.get(k) == self.last_name):
                self.last_name = v
            elif (dic.get(k) == self.age):
                self.age = v
