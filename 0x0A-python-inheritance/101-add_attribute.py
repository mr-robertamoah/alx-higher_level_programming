#!/usr/bin/python3

"""
Contains the add_attribute function
"""


def add_attribute(obj, name, value):
    """ Tries to add an attribute to an object """
    cls = obj.__class__
    slots = getattr(cls, "__slots__", None)

    if (slots and name not in slots) or\
       (not hasattr(cls, "__setattr__")) or\
       isinstance(obj, (int, float, str, tuple, frozenset)):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
