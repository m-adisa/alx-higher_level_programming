#!/usr/bin/python3
"""This is the base module for the project.
It contains the definition of class Base which other classes wil
build on
"""


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
