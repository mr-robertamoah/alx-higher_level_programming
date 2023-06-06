#!/usr/bin/python3

"""
A module containing a Rectangle class

"""


class Rectangle():
    """
    Rectangle class with height and width attributes

    """
    number_of_instances = 0
    print_symbol = "#"

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

        Rectangle.number_of_instances += 1
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

    def area(self):
        """
        Calculate the area of the Rectangle

        Returns:
            int: results of the product of width and height
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the Rectangle

        Returns:
            int: results of adding the length of all four sides
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Print Rectangle using #

        Returns:
            str: formatted string
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        hash_str = str(self.print_symbol)
        hash_list = []
        for i in range(self.__height):
            for j in range(self.__width):
                hash_list.append(hash_str)
            if i + 1 != self.__height:
                hash_list.append("\n")

        return "".join(hash_list)

    def __repr__(self):
        """
        Print expression for instantiating another Rectangle

        Returns:
            str: formatted string
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print message on deletion of instance of Rectangle

        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Checks which rectangle is bigger between two

        Args:
            rect_1 (Rectangle): an instance of Rectangle
            rect_2 (Rectangle): an instance of Rectangle
        Returns:
            <class Rectangle>
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2

        return rect_1
