#!/usr/bin/python3

"""
This module contains a Square class

"""


class Square:
    """
    This is a class representing a square

    Attributes:
        __size (int): this is an integer representing the length of a side
    """
    def __init__(self, size=0):
        """
        This is called when the class is initialized

        Args:
            size (int): this is used to initialize the __size private attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates the area of the square the class represent

        Returns:
            int: area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        A getter for the __size private instance attribute

        Returns:
            int: the length of a side of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        A setter for the __size private instance attribute

        Args:
            value (int): used to set the size of the Square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """
        Prints a square using '#'

        """
        if self.__size > 0:
            for i in range(self.__size):
                print("{}".format("#" * self.__size))
        else:
            print()
