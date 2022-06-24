#!/usr/bin/python3
"""class Square that define a square"""


class Square:
    """Represents a aquare.
    Private instance attribute: size
        -property def size(self)
        -property setter def size(self, value)
    Instantiation with optional size.
    Public instance methid:def area size(self)
    Public instance meethod: def my_print(self)
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Retrieves the size
        Arg:
            self
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value
        Args:
            self, value

        return:
            value of size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area
        Arg:
            self
        """
        return self.__size ** 2

    def my_print(self):
        """Print to stdout the square with character #.
        Arg:
            self
        """
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
