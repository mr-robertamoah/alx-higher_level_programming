#!/usr/bin/python3

"""
Contains a Rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """ A Base with a __init__ method """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializing class or instance attributes

        Args:
            id (int): an integer assignable to self.id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ get the value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the value for width """
        if type(value) is not int:
            Rectangle.raiseNotIntegerError("width")
        if value <= 0:
            Rectangle.raiseValueLessThanOrEqualToZeroError("width")

        self.__width = value

    @property
    def height(self):
        """ get the value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the value for height """
        if type(value) is not int:
            Rectangle.raiseNotIntegerError("height")
        if value <= 0:
            Rectangle.raiseValueLessThanOrEqualToZeroError("height")

        self.__height = value

    @property
    def x(self):
        """ get the value of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set the value for x """
        if type(value) is not int:
            Rectangle.raiseNotIntegerError("x")
        if value < 0:
            Rectangle.raiseValueLessThanZeroError("x")

        self.__x = value

    @property
    def y(self):
        """ get the value of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ set the value for y """
        if type(value) is not int:
            Rectangle.raiseNotIntegerError("y")
        if value < 0:
            Rectangle.raiseValueLessThanZeroError("y")

        self.__y = value

    @staticmethod
    def raiseNotIntegerError(propName):
        """
        raise a TypeError when a property is being set to a non int
        """

        raise TypeError("{} must be an integer".format(propName))

    @staticmethod
    def raiseValueLessThanZeroError(propName):
        """
        raise a ValueError when a property is being set to a
        number which is less than 0
        """

        raise ValueError("{} must be >= 0".format(propName))

    @staticmethod
    def raiseValueLessThanOrEqualToZeroError(propName):
        """
        raise a ValueError when a property is being set to a
        number which is less than or equal to 0
        """

        raise ValueError("{} must be > 0".format(propName))

    def area(self):
        """
        Calculate the area of the rectangle
        """

        return (self.__width * self.__height)

    def display(self):
        """
        display the rectangle with # symbol
        based on the width and height
        """

        for i in range(self.__y):
            print()

        line = "#" * self.__width
        spaces = " " * self.__x
        for i in range(self.__height):
            print(spaces + line)

    def __str__(self):
        """ return a string representation of this instance """

        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
                 {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """ update attributes of an instance in a certain order """

        for key, value in enumerate(args):
            if key == 0:
                self.id = value
            elif key == 1:
                self.width = value
            elif key == 2:
                self.height = value
            elif key == 3:
                self.x = value
            elif key == 4:
                self.y = value

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "width":
                self.width = value
            elif key == "height":
                self.height = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value

    def to_dictionary(self):
        """ Return a dictionary representation of rectangle instance """

        rectangle_dict = {}
        rectangle_dict["id"] = self.id
        rectangle_dict["width"] = self.width
        rectangle_dict["height"] = self.height
        rectangle_dict["x"] = self.x
        rectangle_dict["y"] = self.y
        return rectangle_dict
