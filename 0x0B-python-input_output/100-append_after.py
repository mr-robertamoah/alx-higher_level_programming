#!/usr/bin/python3

"""
Contains append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Append new_string to a file with filename after
    search_string
    """
    content = ""
    with open(filename, "r") as file:
        for line in file:
            content += line
            if search_string in line:
                content += new_string

    with open(filename, "w") as file:
        file.write(content)
