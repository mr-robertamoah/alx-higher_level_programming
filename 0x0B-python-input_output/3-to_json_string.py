#!/usr/bin/python3

"""
Contains to_json_string function
"""

import json


def to_json_string(my_obj):
    """
    Convert an object to a json string

    Args:
        my_obj (object): object to be serialized
    """

    obj_str = json.dumps(my_obj)
    return obj_str
