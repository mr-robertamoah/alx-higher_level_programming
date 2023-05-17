#!/usr/bin/python3

def number_keys(a_dictionary):
    if isinstance(a_dictionary, dict):
        return len(list(a_dictionary))
