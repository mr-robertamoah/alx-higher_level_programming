#!/usr/bin/python3

"""
Contains a LockedClass which only allows a specific
instance attribute

"""


class LockedClass:
    """
    Allows only first_name attribute to set to its instances

    """
    __slots__ = ('first_name', )

    def __init__(self):
        """ Initializes the object """
        self.first_name = None

    def __setattr__(self, name, value):
        """ Overrides the __setattr__ """

        if name != 'first_name':
            raise AttributeError(f"'LockedClass' object has no attribute "
                                 "'{name}'")
        super().__setattr__(name, value)
