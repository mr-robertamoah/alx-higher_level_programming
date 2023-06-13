#!/usr/bin/python3

"""
Contains load_from_json_file function
"""

import json


def load_from_json_file(filename):
    """
    Load json from file and convert to python object

    Args:
        filename (str): name of or path to the file
    """

    with open(filename, "r") as file:
        obj = json.load(file)
        return obj
