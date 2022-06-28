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

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a rectangle instance, filled with the '#' character/
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

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

    def area(self):
        """Calculate the area of a rectangle instance
        Args:
            self
        Return:
            Area (height * width)
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a rectangle
        Args:
            self
        Return:
            Perimeter - 2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
