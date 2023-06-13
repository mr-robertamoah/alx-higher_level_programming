#!/usr/bin/python3

"""
Contains class_to_json function
"""


def class_to_json(obj):
    """
    Returns the the dictionary description of obj

    Args:
        obj (list | dict | str | int | bool): object from which
            dictionary description is gotten
    """

    return obj.__dict__
