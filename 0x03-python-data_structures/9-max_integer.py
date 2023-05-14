#!/usr/bin/python3
def max_integer(my_list=[]):
    """
        If the list is empty, return None
        You can assume that the list only contains integers
        You are not allowed to import any module
        You are not allowed to use the builtin max()
    """
    max_int = 0
    if isinstance(my_list, list) and len(my_list) > 0:
        for i in my_list:
            if i == 0 or i > max_int:
                max_int = i
        return max_int
