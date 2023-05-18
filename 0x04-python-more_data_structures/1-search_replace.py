#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if isinstance(my_list, list) and len(my_list):
        new_list = my_list.copy()
        for k, v in enumerate(new_list):
            if v == search:
                new_list[k] = replace
        return new_list
    else:
        return my_list
