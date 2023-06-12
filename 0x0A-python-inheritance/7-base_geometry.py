#!/usr/bin/python3

"""
Contains a BaseGeometry class
"""


class BaseGeometry():
    """
    A base geometry class
    """

    def area(self):
        """ Raises Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value as an integer  """

        if type(value) is not int:
            raise TypeError("<name> must be an integer")

        if value <= 0:
            raise ValueError("<name> must be greater than 0")
