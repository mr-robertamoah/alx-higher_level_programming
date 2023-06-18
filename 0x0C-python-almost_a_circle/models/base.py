#!/usr/bin/python3

"""
Contains a Base class
"""


class Base():
    """ A Base with a __init__ method """

    __nb_objects = 0

    def __init__ (self, id=None):
        """
        initializing class or method attributes

        Args:
            id (int): an integer assignable to self.id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

