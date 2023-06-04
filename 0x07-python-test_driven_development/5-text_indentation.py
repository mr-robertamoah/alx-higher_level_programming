#!/usr/bin/python3

"""
Contains text_indentation function that indents a string
based on some characters

"""


def text_indentation(text):
    """
    Prints text with newlines after characters such as . ? and :

    Args:
        text (str): string to be indented
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    mini_text = ""
    for c in text:
        mini_text += c
        if c in ".?:":
            mini_text = mini_text.strip()
            print(mini_text, end="\n\n")
            mini_text = ""

    if mini_text:
        print(mini_text.strip(), end="")
