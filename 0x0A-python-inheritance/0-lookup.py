#!/usr/bin/python3

"""
Contains the lookup function that returns attributes
of an object
"""


def lookup(obj):
    """
    Returns the all available attributes on obj

    Args:
        obj (<class object>); python object
    """
    return dir(obj)
