#!/usr/bin/python3

"""
Contains print_square function that uses # to print square

"""


def print_square(size):
    """
    Prints a square with length of size using #

    Args:
        size (int): length of the side of a square
    """

    if (isinstance(size, float) and size < 0) or not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
