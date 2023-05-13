#!/usr/bin/python3
def element_at(my_list, idx):
    number_of_elem = len(my_list)
    if number_of_elem == 0 or idx < 0 or number_of_elem - 1 < idx:
        return None

    return my_list[idx]
