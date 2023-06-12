#!/usr/bin/python3

"""
Contains a Rectangle class
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class extending the BaseGeometry class
    """

    def __init__(self, width, height):
        """ Initializes private attributes """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
