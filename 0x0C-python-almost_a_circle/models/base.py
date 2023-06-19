#!/usr/bin/python3

"""
Contains a Base class
"""

import json
import os


class Base():
    """ A Base with a __init__ method """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializing class or method attributes

        Args:
            id (int): an integer assignable to self.id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the json string for list_dictionaries """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ returns the json string for list_dictionaries """

        with open(f"{cls.__name__}.json", "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = []
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())

                string = cls.to_json_string(list_dict)

                file.write(string)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list version fo the json_string """

        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create an instance of the class """

        if issubclass(cls, Base):
            if cls.__name__ == "Base":
                return Base(dictionary.get("id", None))

            if cls.__name__ == "Square":
                obj = cls(1)
            else:
                obj = cls(1, 1)

            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """ load, create and return a list of instances from file """

        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r") as file:
            json_string = file.read()

            dict_list = cls.from_json_string(json_string)

            return [cls.create(**i) for i in dict_list]
