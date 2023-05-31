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
