#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
        Return a new list with True or False, depending on
        whether the integer at the same position in the original
        list is a multiple of 2
        The new list should have the same size as the original list
        You are not allowed to import any module
    """
    if isinstance(my_list, list):
        if len(my_list) > 0:
            new_list = [b % 2 == 0 for b in my_list]
            return new_list
        else:
            return []
