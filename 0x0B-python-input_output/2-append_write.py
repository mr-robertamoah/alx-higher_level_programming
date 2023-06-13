#!/usr/bin/python3

"""
Contains append_write function
"""


def append_write(filename="", text=""):
    """
    Append a text file with UTF8 encoding

    Args:
        filename (str): name of or path to file
        text (str): string to append to file
    """
    if not isinstance(text, str):
        return 0

    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)

    return len(text)
