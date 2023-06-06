#!/usr/bin/python3

"""
A module containing a Rectangle class

"""


class Rectangle():
    """
    Rectangle class with height and width attributes

    """

    def __init__(self, width=0, height=0):
        """
        Initiates the private properties

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Gives access to the width private property

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value of the width property

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Gives access to the height property

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the value of the height property

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
