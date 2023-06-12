#!/usr/bin/python3

"""
Contains a My_list class that inherits from list
"""


class MyList(list):
    """
    Inherits list object
    """

    def print_sorted(self):
        """
        Prints list in sorted form
        """
        print(sorted(self.copy()))
