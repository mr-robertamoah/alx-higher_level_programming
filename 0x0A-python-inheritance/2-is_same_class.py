#!/usr/bin/python3

"""
Contains is_same_class function
"""


def is_same_class(obj, a_class):
    """
    Returns true of false if obj is same class as a_class
    """

    return (type(obj) is a_class)
