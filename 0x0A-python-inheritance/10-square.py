#!/usr/bin/python3

"""
Contains a Square class
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A Square class extending the Rectangle class
    """

    def __init__(self, size):
        """ Initializes private attributes """
        self.integer_validator("size", size)

        super().__init__(size, size)

        self.__size = size

    def area(self):
        """ Calculates the area of the Square """
        return (self.__size * self.__size)
