#!/usr/bin/python3

"""
Contains a say_my_name function that prints a string
containing the first and last names

"""


def say_my_name(first_name, last_name=""):
    """
    Prints a string containing the first_name and last_name

    Args:
        first_name (str): the first name
        last_name (str): the last name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
