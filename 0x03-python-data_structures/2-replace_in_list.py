#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    number_of_elem = len(my_list)
    if number_of_elem == 0 or idx < 0 or number_of_elem - 1 < idx:
        return my_list

    my_list[idx] = element
    return my_list
