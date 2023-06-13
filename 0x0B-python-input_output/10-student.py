#!/usr/bin/python3

"""
Contains a Student class
"""


class Student():
    """ Student Class with instance variables """

    def __init__(self, first_name, last_name, age):
        """ Instantiation of instance variables """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns dictionary representation of Student """

        if isinstance(attrs, list):
            return {key: self.__dict__[key]
                    for key in self.__dict__ if key in attrs}
        return self.__dict__
