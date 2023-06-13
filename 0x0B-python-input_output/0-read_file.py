#!/usr/bin/python3

"""
Contains read_file function
"""


def read_file(filename=""):
    """
    Read a text file with UTF8 encoding

    Args:
        filename (str): name of or path to file
    """

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
