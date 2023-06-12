#!/usr/bin/python3

"""
Contains inherited_from function
"""


def inherits_from(obj, a_class):
    """
    Returns true of false if obj inherites from a_class
    on any level
    """

    for cls in type(obj).__mro__:
        if not cls is a_class and issubclass(cls, a_class):
            return True

    return False
