#!/usr/bin/python3
"""class that defines a square"""


class Square:
    """class defining a square"""
    def __init__(self, size=0):
        """initialize a square"""
        self.size = size

    @property
    def size(self):
        """Retrieving the value of size"""
        return self.__size

    @size.setter
    def size(size, value):
        """sets the conditions of the value of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2
