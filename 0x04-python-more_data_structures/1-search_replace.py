#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if isinstance(my_list, list) and len(my_list):
        new_list = my_list.copy()
        if search in new_list:
            new_list[new_list.index(search)] = replace
        return new_list
    else:
        return my_list
