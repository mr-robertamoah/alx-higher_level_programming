#!/usr/bin/python3

"""
Module containing an add function for integers

"""


def add_integer(a, b=98):
    """
    Add two integers

    Args:
        a (int): first integer argument
        b (int): second integer argument

    Returns:
        int: addition of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
