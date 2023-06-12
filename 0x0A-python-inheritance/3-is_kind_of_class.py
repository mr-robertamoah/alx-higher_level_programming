#!/usr/bin/python3

"""
Contains is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    Returns true of false if obj is same class as a_class
    of inherits from it
    """

    return (isinstance(obj, a_class))
