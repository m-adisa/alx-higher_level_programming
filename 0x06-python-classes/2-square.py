#!/usr/bin/python3
"""class defines a square"""


class Square:
    """class Square defining a square"""

    def __init__(self, size=0):
        """initialize the square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
