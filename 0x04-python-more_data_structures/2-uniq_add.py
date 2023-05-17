#!/usr/bin/python3

def uniq_add(my_list=[]):
    if isinstance(my_list, list):
        sum_i = 0
        if len(my_list):
            for i in list(set(my_list)):
                sum_i += i
        return sum_i
