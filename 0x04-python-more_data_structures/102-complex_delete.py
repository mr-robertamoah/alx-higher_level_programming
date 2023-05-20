#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if isinstance(a_dictionary, dict):
        del_list = []
        for k, v in a_dictionary.items():
            if v == value:
                del_list.append(k)

        for k in del_list:
            del a_dictionary[k]
    return a_dictionary
