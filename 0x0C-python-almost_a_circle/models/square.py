#!/usr/bin/python3
"""Module containing the definition of class Square
class Square inherits from class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square is a special kind of rectangle with
    equal height and width. This class inherits all methods
    and attributes from the class Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of the Square class
        Args:
            - size: height and width must be assigned to the value of size
            - x
            - y
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size value as the equivalent of
        height and width
        """

        self.width = value
        self.height = value

    def __str__:
        "Returns the string representation of the square by its attributes"""

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
