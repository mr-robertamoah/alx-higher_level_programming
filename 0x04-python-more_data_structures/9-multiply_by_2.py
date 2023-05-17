#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    if isinstance(a_dictionary, dict):
        return dict((k, v*2) for k, v in a_dictionary.items())
    return a_dictionary
