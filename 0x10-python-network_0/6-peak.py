#!/usr/bin/python3

"""contains find_peak function"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""

    if isinstance(list_of_integers, list) and list_of_integers is not None and\
            len(list_of_integers) > 0:
        len_list = len(list_of_integers)
        mid = ((len_list - 0) // 2) + 0
        mid = int(mid)
        if len_list == 1:
            return list_of_integers[0]
        if len_list == 2:
            return max(list_of_integers)
        if list_of_integers[mid] >= list_of_integers[mid - 1] and\
                list_of_integers[mid] >= list_of_integers[mid + 1]:
            return list_of_integers[mid]
        if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
            return find_peak(list_of_integers[mid:])
        if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            return find_peak(list_of_integers[:mid])
