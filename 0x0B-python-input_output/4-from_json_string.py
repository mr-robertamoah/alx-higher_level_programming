#!/usr/bin/python3

"""
Contains from_json_string function
"""

import json


def from_json_string(my_str):
    """
    Convert a json string to a python object

    Args:
        my_str (json string): string to be deserialized
    """

    obj = json.loads(my_str)
    return obj
