#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    number_of_elem = len(my_list)
    if number_of_elem == 0 or idx < 0 or number_of_elem - 1 < idx:
        return my_list
    for i in range(len(my_list)):
        new_list.append(my_list[i])
    new_list[idx] = element
    return new_list
