#!/usr/bin/python3
def max_integer(my_list=[]):
    """
        If the list is empty, return None
        You can assume that the list only contains integers
        You are not allowed to import any module
        You are not allowed to use the builtin max()
    """
    if isinstance(my_list, list) and len(my_list) > 0:
        max_int = 0
        for i in range(len(my_list)):
            if i == 0 or my_list[i] > max_int:
                max_int = my_list[i]
        return max_int
