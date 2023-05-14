#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
        If idx is negative or out of range, nothing change
        (returns the same list)
        You are not allowed to use pop()
        You are not allowed to import any module
    """
    if isinstance(my_list, list):
        my_list_len = len(my_list)
        if idx >= 0 and my_list_len > idx:
            for i in range(my_list_len):
                if i == idx:
                    my_list.remove(my_list[idx])
                    break
            return my_list
        else:
            return my_list
