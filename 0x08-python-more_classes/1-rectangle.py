#!/usr/bin/python3
"""module defines a rectangles
1) Rectangle: defines a retangle by width
"""


class Rectangle:
    """The class defines a rectangle by width and height."""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle instance
        Args:
            width - width of the rectangle
            height - height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle
        Args: self
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a rectangle
        Args:
            value - value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle
        Args: self
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a ractangle
        Args:
            value - value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value