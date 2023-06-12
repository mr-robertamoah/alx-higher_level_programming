#!/usr/bin/python3

"""
Contains MyInt class
"""


class MyInt(int):
    """
    Extends int class
    """

    def __eq__(self, other):
        """ inventing == implemetation """
        if isinstance(other, MyInt):
            return self != other
        return False

    def __ne__(self, other):
        """ inventing != implemetation """
        return not self.__eq__(other)
