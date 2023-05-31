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
    def __init__(self, size):
        """
        This is called when the class is initialized

        Args:
            size (int): this is used to initialize the __size private attribute
        """
        self.__size = size
