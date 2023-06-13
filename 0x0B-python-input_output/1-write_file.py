#!/usr/bin/python3

"""
Contains write_file function
"""


def write_file(filename="", text=""):
    """
    Write a text file with UTF8 encoding

    Args:
        filename (str): name of or path to file
        text (str): string to write to file
    """

    nb_chars = 0

    if not isinstance(text, str):
        return nb_chars

    with open(filename, "w", encoding="utf-8") as file:
        nb_chars = file.write(text)

    return nb_chars
