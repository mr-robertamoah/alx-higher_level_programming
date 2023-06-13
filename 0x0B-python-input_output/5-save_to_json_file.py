#!/usr/bin/python3

"""
Contains from_json_string function
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Convert a json string to a python object

    Args:
        my_obj (object): object to save to file
        filename (str): name of or path to the file
    """

    with open(filename, "w") as file:
        json.dump(my_obj, file)
