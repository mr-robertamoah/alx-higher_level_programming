#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        for i in range(1, len(my_list) + 1):
            j = i * -1
            print("{:d}".format(my_list[j]))
        my_list.reverse()
