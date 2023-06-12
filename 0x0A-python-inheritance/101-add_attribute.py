#!/usr/bin/python3

"""
Contains the add_attribute function
"""


def add_attribute(obj, name, value):
    """ Tries to add an attribute to an object """
    cls = obj.__class__
    slots = getattr(cls, "__slots__", None)

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
