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

    def update(self, *args, **kwargs):
        """The public method assigns values to the attributes.
        Uses kwargs if args exists and is not empty.
        """

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
