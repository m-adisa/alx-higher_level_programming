#!/usr/bin/python3
"""This is the base module for the project.
It contains the definition of class Base which other classes wil
build on
"""
import json


class Base:
    """Class with:
    Private class attribute: __nbobjects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation of the class Base
        Args:
            - id: instance id
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the json representation of the argument
        Args:
            - list_dictionaries
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file
        Args:
            - cls
            - list_objs
        """
        
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsfile:
            if list_objs is None:
                jsfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsfile.write(Base.to_json_string(list_dicts))
