#!/usr/bin/python3
"""Module 9-student.py
1) class Student
"""


class Student:
    """A clss that define a student by
        - first name
        - last name
        - age
    public method: to_json
    """

    def __init__(self, first_name, last_name, age):
        """Instantiation of the class
            - first_name, last_name, age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary repersentation of an object"""
        my_dict = dict()
        if type(attrs) is list and all(type(elem) is str for elem in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        Args:
            - self
            - json
        """
        for x in json:
            self.__dict__.update({x: json[x]})
