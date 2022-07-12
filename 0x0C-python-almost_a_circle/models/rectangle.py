#!/usr/bin/python3
"""Module containing the definition of class Rectangle
class Rectangle inherits from class Base
"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle inheriting from class Base
    Containing all attributes and methods required"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the class Rectangle
        Args:
            - width (int)
            - height (int)
            - x (int)
            - y (int)
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width
        Args:
            - self
            - value
        Raises:
            - TypeError for wrong width type
            - ValueError for width less or equal to zero
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height
        Args:
            - self
            - value
        Raises:
            - TypeError for wrong height type
            - ValueError for height less or equal to zero
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the x attribute"""

        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x
        Args:
            - self
            - value
        Raises:
            - TypeError for wrong x type
            - ValueError for x less or equal to zero
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves the y attribute"""

        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y
        Args:
            - self
            - value
        Raises:
            - TypeError for wrong y type
            - ValueError for y less or equal to zero
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the rectangle instance
        Area: height x width
        """

        return self.height * self.width

    def display(self):
        """Prints in stdout, the Rectangle instance with the character #
        with dimensions self.height and self.width
        """

        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__:
        """Returns a string representation of the Rectangle object
        Prints all defining variables
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """Method to assign an argument to each attribute"""

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""

        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
