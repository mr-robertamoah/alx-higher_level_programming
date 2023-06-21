#!/usr/bin/python3

"""
Contains BaseTest class
"""


import unittest
import os
import json
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class BaseTest(unittest.TestCase):
    """ Testing Base Class """

    @classmethod
    def tearDown(cls):
        paths = [
                 "Base.json",
                 "Rectangle.json",
                 "Square.json",
                 "Base.csv",
                 "Rectangle.csv",
                 "Square.csv"
                ]
        for path in paths:
            if os.path.exists(path):
                os.remove(path)

    def test_can_initialize_class_with_no_argument(self):
        """ check if Base is properly initialized """
        base = Base()
        self.assertGreater(base.id, 0)

    def test_can_initialize_class_with_one_argument(self):
        """ check if Base is properly initialized """
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_cannot_initialize_class_with_more_than_one_argument(self):
        """ check if Base is properly initialized """
        with self.assertRaises(TypeError) as ctx:
            base = Base(1, 2)

    def test_assignment_to_id_when_value_is_none_on_initialization(self):
        """ check if Base is properly initialized """
        base1 = Base()
        base2 = Base()
        self.assertEqual(base2.id, base1.id + 1)
        base3 = Base()
        self.assertEqual(base3.id, base2.id + 1)

    def test_assignment_to_id_when_value_is_int_on_initialization(self):
        """ check if Base is properly initialized """
        base1 = Base(5)
        self.assertEqual(base1.id, 5)
        base2 = Base(15)
        self.assertEqual(base2.id, 15)

    def test_assignment_to_id_when_value_is_int_after_initialization(self):
        """ check if Base is properly initialized """
        base1 = Base(5)
        self.assertEqual(base1.id, 5)
        base1.id = 15
        self.assertEqual(base1.id, 15)

    def test_assign_none_to_id(self):
        """ testing assignment to id """

        self.assertEqual(Base(None).id, Base(None).id - 1)

    def test_assign_float_to_id(self):
        """ testing assignment to id """

        base = Base(1.1)
        self.assertEqual(base.id, 1.1)

    def test_assign_string_to_id(self):
        """ testing assignment to id """

        base = Base("1.1")
        self.assertEqual(base.id, "1.1")

    def test_assign_list_to_id(self):
        """ testing assignment to id """

        base = Base([1.1])
        self.assertEqual(base.id, [1.1])

    def test_assign_tuple_to_id(self):
        """ testing assignment to id """

        base = Base((1.1, ))
        self.assertEqual(base.id, (1.1, ))

    def test_assign_set_to_id(self):
        """ testing assignment to id """

        base = Base({1, 2})
        self.assertEqual(base.id, {1, 2})

    def test_assign_dict_to_id(self):
        """ testing assignment to id """

        base = Base({'a': 1.1})
        self.assertEqual(base.id, {'a': 1.1})

    def test_assign_frozenset_to_id(self):
        """ testing assignment to id """

        base = Base(frozenset({1, 2}))
        self.assertEqual(base.id, frozenset({1, 2}))

    def test_assign_bool_to_id(self):
        """ testing assignment to id """

        base = Base(True)
        self.assertEqual(base.id, True)

    def test_assign_complex_to_id(self):
        """ testing assignment to id """

        base = Base(complex(10))
        self.assertEqual(base.id, complex(10))

    def test_assign_nan_to_id(self):
        """ testing assignment to id """

        base = Base(float("nan"))
        self.assertNotEqual(base.id, float("nan"))

    # to_json_string --------------------------

    def test_cannot_call_to_json_string_with_no_arguments(self):
        """ testing to_json_string static method """

        r = Rectangle(1, 3)
        with self.assertRaises(TypeError) as ctx:
            json_string = Base.to_json_string()

    def test_cannot_call_to_json_string_with_more_than_one_arguments(self):
        """ testing to_json_string static method """

        r = Rectangle(1, 3)
        with self.assertRaises(TypeError) as ctx:
            json_string = Base.to_json_string([r], [])

    def test_can_call_to_json_string_with_empty_list(self):
        """ testing to_json_string static method """

        json_string = Base.to_json_string([])
        self.assertIsInstance(json_string, str)
        self.assertEqual(json_string, "[]")

    def test_can_call_to_json_string_with_none(self):
        """ testing to_json_string static method """

        json_string = Rectangle.to_json_string(None)
        self.assertIsInstance(json_string, str)
        self.assertEqual(json_string, "[]")

    def test_to_json_string_returns_none_when_with_neither_list_nor_none(self):
        """ testing to_json_string static method """

        json_string = Base.to_json_string(1)
        self.assertEqual(json_string, "1")

        json_string = Base.to_json_string(True)
        self.assertEqual(json_string, "true")

        json_string = Base.to_json_string(4.64)
        self.assertEqual(json_string, "4.64")

        json_string = Base.to_json_string((1, ))
        self.assertEqual(json_string, "[1]")

        with self.assertRaises(TypeError) as ctx:
            json_string = Base.to_json_string({1, 2})

        json_string = Base.to_json_string("string")
        self.assertEqual(json_string, '"string"')

        json_string = Base.to_json_string({"string": 1})
        self.assertEqual(json_string, '{"string": 1}')

        with self.assertRaises(TypeError) as ctx:
            json_string = Base.to_json_string(frozenset({1, 2}))

    def test_to_json_string_returns_string(self):
        """ testing to_json_string static method """

        r = Rectangle(1, 3)
        json_string = Base.to_json_string([r.to_dictionary()])
        self.assertIsInstance(json_string, str)

    def test_to_json_string_can_be_called_on_Rectangle_and_Square(self):
        """ testing to_json_string static method """

        r = Rectangle(1, 3)
        json_string = Base.to_json_string([r.to_dictionary()])
        self.assertEqual(
                         json_string,
                         Rectangle.to_json_string([r.to_dictionary()]))
        self.assertEqual(
                         json_string,
                         Square.to_json_string([r.to_dictionary()]))

    # save_to_file ------------------------------------------

    def test_file_is_overwritten_when_save_to_file_is_called(self):
        """ testing save_to_file class method """

        string = "hi, there"
        with open("Rectangle.json", "w") as file:
            file.write(string)

        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as file:
            self.assertNotEqual(file.read(), string)

    def test_file_is_created_when_save_to_file_is_called(self):
        """ testing save_to_file class method """

        string = "Rectangle.json"
        if os.path.exists(string):
            os.remove(string)

        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(os.path.exists(string))
            self.assertEqual(file.read(), json.dumps([r.to_dictionary()]))

    def test_can_save_when_save_to_file_is_called_none(self):
        """ testing save_to_file class method """

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_can_save_when_save_to_file_is_called_with_empty_list(self):
        """ testing save_to_file class method """

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_can_save_in_base_json(self):
        """ testing save_to_file class method """

        Base.save_to_file([])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_can_save_in_rectangle_json(self):
        """ testing save_to_file class method """

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_can_save_in_square_json(self):
        """ testing save_to_file class method """

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_calling_save_to_file_with_no_arguments(self):
        """ testing save_to_file class method """

        with self.assertRaises(TypeError) as ctx:
            Base.save_to_file()

        with self.assertRaises(TypeError) as ctx:
            Square.save_to_file()

        with self.assertRaises(TypeError) as ctx:
            Rectangle.save_to_file()

    def test_calling_save_to_file_with_more_than_one_argument(self):
        """ testing save_to_file class method """

        with self.assertRaises(TypeError) as ctx:
            Base.save_to_file([], [])

        with self.assertRaises(TypeError) as ctx:
            Square.save_to_file([], [])

        with self.assertRaises(TypeError) as ctx:
            Rectangle.save_to_file([], [])

    def test_the_use_of_one_object_list_as_argument(self):
        """ testing save_to_file class method """

        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), json.dumps([r.to_dictionary()]))

        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as file:
            content = file.read()
            r = Square.create(Square.from_json_string(content))[0]
            self.assertEqual(content, json.dumps([r.to_dictionary()]))

    def test_cannot_use_base_class_object_in_list_as_argument(self):
        """ testing save_to_file class method """

        r2 = Base(3)
        with self.assertRaises(AttributeError):
            Rectangle.save_to_file([r2])
            with open("Rectangle.json", "r") as file:
                self.assertEqual(file.read(), json.dumps([r2.to_dictionary()]))

    def test_the_use_of_multiple_same_base_object_list_as_argument(self):
        """ testing save_to_file class method """

        r1 = Square(1, 2)
        r2 = Square(3, 4)
        Square.save_to_file([r1, r2])
        with open("Square.json", "r") as file:
            self.assertEqual(
                             file.read(),
                             json.dumps([
                                         r1.to_dictionary(),
                                         r2.to_dictionary()]))

        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                             file.read(),
                             json.dumps([
                                         r1.to_dictionary(),
                                         r2.to_dictionary()]))

    def test_the_use_of_multiple_differemt_base_object_list_as_argument(self):
        """ testing save_to_file class method """

        r1 = Rectangle(1, 2)
        r2 = Square(3, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                             file.read(),
                             json.dumps([
                                         r1.to_dictionary(),
                                         r2.to_dictionary()]))

    def test_the_use_of_multiple_different_objects_list_as_argument(self):
        """ testing save_to_file class method """

        r1 = Rectangle(1, 2)
        r2 = "string"
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file([r1, r2])

        r2 = 1
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file([r1, r2])

        r2 = 2.4
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file([r1, r2])

        r2 = (1, )
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file([r1, r2])

        r2 = {1, 2}
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file([r1, r2])

        r2 = {"a": 1, "b": 3}
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file([r1, r2])

        r2 = frozenset({2, 3})
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file([r1, r2])

    def test_the_use_non_list_as_argument(self):
        """ testing save_to_file class method """

        r = "string"
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file(r)

        r = 1
        with self.assertRaises(TypeError) as ctx:
            Rectangle.save_to_file(r)

        r = 3.5
        with self.assertRaises(TypeError) as ctx:
            Rectangle.save_to_file(r)

        r = (1, )
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file(r)

        r = {1, 3}
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file(r)

        r = {"a": 1, "v": 3}
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file(r)

        r = frozenset({1, 3})
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file(r)

    # from_json_string ------------------------------

    def test_from_json_string_cannot_be_called_with_no_arguments(self):
        """ testing from_json_string static method """

        with self.assertRaises(TypeError) as ctx:
            string = Base.from_json_string()

    def tes_cannot_be_called_with_more_than_one_argument(self):
        """ testing from_json_string static method """

        with self.assertRaises(TypeError) as ctx:
            string = Base.from_json_string("[]", "[]")

    def test_can_call_from_json_string_with_empty_string(self):
        """ testing from_json_string static method """

        string = Base.from_json_string("")
        self.assertEqual(string, [])

    def test_can_call_from_json_string_with_none(self):
        """ testing from_json_string static method """

        string = Base.from_json_string(None)
        self.assertEqual(string, [])

    def test_can_call_from_json_string_with_json_list(self):
        """ testing from_json_string static method """

        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        json_string = Base.to_json_string([
                                           r1.to_dictionary(),
                                           r2.to_dictionary()])
        json_list = Base.from_json_string(json_string)
        self.assertEqual(
                         json_string,
                         json.dumps([
                                     r1.to_dictionary(),
                                     r2.to_dictionary()]))
        self.assertEqual(
                         json_list,
                         [
                          r1.to_dictionary(),
                          r2.to_dictionary()])

    def test_using_non_strings_can_call_from_json_string(self):
        """ testing from_json_string static method """

        with self.assertRaises(TypeError) as ctx:
            string = Base.from_json_string(1)

        with self.assertRaises(TypeError) as ctx:
            string = Base.from_json_string(1.2)

        with self.assertRaises(TypeError) as ctx:
            string = Base.from_json_string([1, 2])

        with self.assertRaises(TypeError) as ctx:
            string = Base.from_json_string((1, ))

        with self.assertRaises(TypeError) as ctx:
            string = Base.from_json_string({1, 2})

        with self.assertRaises(TypeError) as ctx:
            string = Base.from_json_string({"a": 1})

        with self.assertRaises(TypeError) as ctx:
            string = Base.from_json_string(frozenset({1, 2}))

    def test_using_json_of_non_lists_can_call_from_json_string(self):
        """ testing from_json_string static method """

        item = "1"
        output = Base.from_json_string(json.dumps(item))
        self.assertEqual(output, item)

        item = 1
        output = Base.from_json_string(json.dumps(item))
        self.assertEqual(output, item)

        item = 1.5
        output = Base.from_json_string(json.dumps(item))
        self.assertEqual(output, item)

        item = {"a": 1}
        output = Base.from_json_string(json.dumps(item))
        self.assertEqual(output, item)

        item = [1, 2]
        output = Base.from_json_string(json.dumps(item))
        self.assertEqual(output, item)

        item = (1, )
        output = Base.from_json_string(json.dumps(item))
        self.assertNotEqual(output, item)

    def test_different_classes_can_call_from_json_string(self):
        """ testing from_json_string static method """

        string = Base.from_json_string(None)
        self.assertEqual(string, [])

        string = Rectangle.from_json_string(None)
        self.assertEqual(string, [])

        string = Square.from_json_string(None)
        self.assertEqual(string, [])

    # create class method -----------------------------------

    def test_cannot_create_with_positional_arguments(self):
        """ testing create class method """

        with self.assertRaises(TypeError):
            rectangle = Rectangle.create(1, 2)

    def test_can_create_without_an_argument(self):
        """ testing create class method """

        rectangle = Rectangle.create()
        self.assertIsInstance(rectangle, Rectangle)

    def test_can_create_rectangle_from_dictionary(self):
        """ testing create class method """

        r = Rectangle(10, 10)
        dictionary = r.to_dictionary()
        rectangle = Rectangle.create(**dictionary)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual(r.id, rectangle.id)

    def test_can_create_square_from_dictionary(self):
        """ testing create class method """

        r = Rectangle(10, 10)
        dictionary = r.to_dictionary()
        square = Square.create(**dictionary)
        self.assertIsInstance(square, Square)
        self.assertEqual(r.id, square.id)

    def test_can_create_base_from_dictionary(self):
        """ testing create class method """

        r = Rectangle(10, 10)
        dictionary = r.to_dictionary()
        base = Base.create(**dictionary)
        self.assertIsInstance(base, Base)
        self.assertEqual(r.id, base.id)

    def test_cannot_create_with_non_dictionary_argument(self):
        """ testing create class method """

        with self.assertRaises(TypeError):
            Rectangle.create(1)

        with self.assertRaises(TypeError):
            Rectangle.create(1.4)

        with self.assertRaises(TypeError):
            Rectangle.create("hey")

        with self.assertRaises(TypeError):
            Rectangle.create((1, ))

        with self.assertRaises(TypeError):
            Rectangle.create([1, 2])

        with self.assertRaises(TypeError):
            Rectangle.create({1, 2})

        with self.assertRaises(TypeError):
            Rectangle.create(frozenset({1, 2}))

        with self.assertRaises(TypeError):
            Rectangle.create(complex(1))

    # load_from_file -------------------------------

    def test_cannot_call_load_from_file_with_arguments(self):
        """ testing load_from_file class method """

        with self.assertRaises(TypeError):
            Base.load_from_file([])

    def test_cannot_save_to_or_load_from_file_depends_on_base_class(self):
        """ testing load_from_file class method """

        r = Base(1)
        with self.assertRaises(AttributeError):
            Base.save_to_file([r])
            items = Base.load_from_file()
            self.assertIsInstance(items, list)
            for i in items:
                self.assertIsInstance(i, Base)

    def test_can_create_instance_of_different_type(self):
        """ testing load_from_file class method """

        r = Rectangle(1, 2)
        self.assertIsInstance(r, Rectangle)
        Square.save_to_file([r])
        items = Square.load_from_file()
        self.assertIsInstance(items, list)
        for i in items:
            self.assertIsInstance(i, Square)

        r = Square(1, 2)
        self.assertIsInstance(r, Square)
        Rectangle.save_to_file([r])
        items = Rectangle.load_from_file()
        self.assertIsInstance(items, list)
        for i in items:
            self.assertIsInstance(i, Rectangle)

    def test_instances_of_load_from_file_depend_on_class_used(self):
        """ testing load_from_file class method """

        r = Base(1)
        with open("Base.json", "w") as file:
            dictionary = {}
            dictionary["id"] = r.id
            json.dump([dictionary], file)

        items = Base.load_from_file()
        self.assertIsInstance(items, list)
        for i in items:
            self.assertIsInstance(i, Base)

        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        items = Rectangle.load_from_file()
        self.assertIsInstance(items, list)
        for i in items:
            self.assertIsInstance(i, Rectangle)

        r = Square(1, 2)
        Square.save_to_file([r])
        items = Square.load_from_file()
        self.assertIsInstance(items, list)
        for i in items:
            self.assertIsInstance(i, Square)

        r1 = Rectangle(1, 2)
        r2 = Square(1, 2)
        Square.save_to_file([r1, r2])
        items = Square.load_from_file()
        self.assertIsInstance(items, list)
        for i in items:
            self.assertIsInstance(i, (Rectangle, Square))

    def test_call_load_from_file_returns_empty_list_if_there_is_no_file(self):
        """ testing load_from_file class method """

        filename = "Rectangle.json"
        if os.path.exists(filename):
            os.remove(filename)

        item = Rectangle.load_from_file()
        self.assertIsInstance(item, list)
        self.assertEqual(len(item), 0)

    def test_call_load_from_file_returns_empty_list_if_there_is_no_file(self):
        """ testing load_from_file class method """

        filename = "Rectangle.json"
        with open(filename, "w") as file:
            json.dump(1, file)
        with self.assertRaises(TypeError):
            Rectangle.load_from_file()

        with open(filename, "w") as file:
            json.dump(1.4, file)
        with self.assertRaises(TypeError):
            Rectangle.load_from_file()

        with open(filename, "w") as file:
            json.dump("string", file)
        with self.assertRaises(TypeError):
            Rectangle.load_from_file()

        with open(filename, "w") as file:
            json.dump((1, ), file)
        with self.assertRaises(TypeError):
            Rectangle.load_from_file()

        with open(filename, "w") as file:
            json.dump({"a": 1}, file)
        with self.assertRaises(TypeError):
            Rectangle.load_from_file()

    # save_to_file_csv -----------------------------

    def test_file_is_overwritten_when_save_to_file_csv_is_called(self):
        """ testing save_to_file_csv class method """

        string = "hi, there"
        with open("Rectangle.csv", "w") as file:
            file.write(string)

        Rectangle.save_to_file_csv([Rectangle(1, 2)])
        with open("Rectangle.csv", "r") as file:
            self.assertNotEqual(file.read(), string)

    def test_file_is_created_when_save_to_file_csv_is_called(self):
        """ testing save_to_file_csv class method """

        string = "Rectangle.csv"
        if os.path.exists(string):
            os.remove(string)

        r = Rectangle(1, 2)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as file:
            self.assertTrue(os.path.exists(string))

    def test_can_save_when_save_to_file_csv_is_called_none(self):
        """ testing save_to_file_csv class method """

        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_can_save_when_save_to_file_csv_is_called_with_empty_list(self):
        """ testing save_to_file_csv class method """

        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_can_save_in_base_csv(self):
        """ testing save_to_file_csv class method """

        Base.save_to_file_csv([])
        with open("Base.csv", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_can_save_in_rectangle_csv(self):
        """ testing save_to_file_csv class method """

        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_can_save_in_square_csv(self):
        """ testing save_to_file_csv class method """

        Square.save_to_file_csv([])
        with open("Square.csv", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_calling_save_to_file_csv_with_no_arguments(self):
        """ testing save_to_file_csv class method """

        with self.assertRaises(TypeError) as ctx:
            Base.save_to_file_csv()

    def test_calling_save_to_file_csv_with_more_than_one_argument(self):
        """ testing save_to_file_csv class method """

        with self.assertRaises(TypeError) as ctx:
            Base.save_to_file_csv([], [])

    def test_the_use_of_one_object_list_as_argument(self):
        """ testing save_to_file_csv class method """

        r = Rectangle(1, 2)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(
                             file.read(),
                             "".join(
                                     str(r.to_dictionary().values())
                                     .replace(" ", "")
                                     .replace("dict_values", "")
                                     .replace("[", "")
                                     .replace("]", "")
                                     .replace("(", "")
                                     .replace(")", "")) + "\n")

    def test_cannot_use_base_class_object_in_list_as_argument(self):
        """ testing save_to_file_csv class method """

        r2 = Base(3)
        with self.assertRaises(AttributeError):
            Rectangle.save_to_file_csv([r2])
            with open("Rectangle.csv", "r") as file:
                self.assertEqual(
                                 file.read(),
                                 json.dumps([r2.to_dictionary().values()]))

    def test_the_use_of_multiple_same_base_object_list_as_argument(self):
        """ testing save_to_file_csv class method """

        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as file:
            self.assertTrue(str([
                                 r1.to_dictionary().values(),
                                 r2.to_dictionary().values()])
                            .find(file.read()))

    def test_cannot_use_multiple_differemt_base_object_list_as_argument(self):
        """ testing save_to_file_csv class method """

        r1 = Rectangle(1, 2)
        r2 = Square(3, 4)
        with self.assertRaises(ValueError):
            Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(
                             file.read(),
                             str(r1.id) + ",1,2,0,0\n")

    def test_the_use_of_multiple_different_objects_list_as_argument(self):
        """ testing save_to_file_csv class method """

        r1 = Rectangle(1, 2)
        r2 = "string"
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file_csv([r1, r2])

        r2 = 1
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file_csv([r1, r2])

        r2 = 2.4
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file_csv([r1, r2])

        r2 = (1, )
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file_csv([r1, r2])

        r2 = {1, 2}
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file_csv([r1, r2])

        r2 = {"a": 1, "b": 3}
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file_csv([r1, r2])

        r2 = frozenset({2, 3})
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file_csv([r1, r2])

    def test_the_use_non_list_as_argument(self):
        """ testing save_to_file_csv class method """

        r = "string"
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file_csv(r)

        r = 1
        with self.assertRaises(TypeError) as ctx:
            Rectangle.save_to_file_csv(r)

        r = 3.5
        with self.assertRaises(TypeError) as ctx:
            Rectangle.save_to_file_csv(r)

        r = (1, )
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file_csv(r)

        r = {1, 3}
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file_csv(r)

        r = {"a": 1, "v": 3}
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file_csv(r)

        r = frozenset({1, 3})
        with self.assertRaises(AttributeError) as ctx:
            Rectangle.save_to_file_csv(r)

    # load_from_file_csv -------------------------------

    def test_cannot_call_load_from_file_csv_with_arguments(self):
        """ testing load_from_file_csv class method """

        with self.assertRaises(TypeError):
            Base.load_from_file_csv([])

    def test_cannot_save_to_or_load_from_file_csv_depends_on_base_class(self):
        """ testing load_from_file_csv class method """

        r = Base(1)
        with self.assertRaises(AttributeError):
            Base.save_to_file([r])
            items = Base.load_from_file_csv()
            self.assertIsInstance(items, list)
            for i in items:
                self.assertIsInstance(i, Base)

    def test_can_create_instance_of_different_type(self):
        """ testing load_from_file_csv class method """

        r = Rectangle(1, 2)
        self.assertIsInstance(r, Rectangle)
        Square.save_to_file([r])
        items = Square.load_from_file_csv()
        self.assertIsInstance(items, list)
        for i in items:
            self.assertIsInstance(i, Square)

        r = Square(1, 2)
        self.assertIsInstance(r, Square)
        Rectangle.save_to_file([r])
        items = Rectangle.load_from_file_csv()
        self.assertIsInstance(items, list)
        for i in items:
            self.assertIsInstance(i, Rectangle)

    def test_instances_of_load_from_file_csv_depend_on_class_used(self):
        """ testing load_from_file_csv class method """

        r = Base(1)
        with open("Base.json", "w") as file:
            dictionary = {}
            dictionary["id"] = r.id
            json.dump([dictionary], file)

        items = Base.load_from_file_csv()
        self.assertIsInstance(items, list)
        for i in items:
            self.assertIsInstance(i, Base)

        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        items = Rectangle.load_from_file_csv()
        self.assertIsInstance(items, list)
        for i in items:
            self.assertIsInstance(i, Rectangle)

        r = Square(1, 2)
        Square.save_to_file([r])
        items = Square.load_from_file_csv()
        self.assertIsInstance(items, list)
        for i in items:
            self.assertIsInstance(i, Square)

        r1 = Rectangle(1, 2)
        r2 = Square(1, 2)
        Square.save_to_file([r1, r2])
        items = Square.load_from_file_csv()
        self.assertIsInstance(items, list)
        for i in items:
            self.assertIsInstance(i, (Rectangle, Square))

    def test_returns_empty_list_if_there_is_no_file(self):
        """ testing load_from_file_csv class method """

        filename = "Rectangle.json"
        if os.path.exists(filename):
            os.remove(filename)

        item = Rectangle.load_from_file_csv()
        self.assertIsInstance(item, list)
        self.assertEqual(len(item), 0)

    def tes_returns_empty_list_for_wrong_file_content(self):
        """ testing load_from_file_csv class method """

        filename = "Rectangle.json"
        with open(filename, "w") as file:
            json.dump(1, file)
            result = Rectangle.load_from_file_csv()
            self.assertEqual(result, [])

        with open(filename, "w") as file:
            json.dump(1.4, file)
            result = Rectangle.load_from_file_csv()
            self.assertEqual(result, [])

        with open(filename, "w") as file:
            json.dump("string", file)
            Rectangle.load_from_file_csv()
            self.assertEqual(result, [])

        with open(filename, "w") as file:
            json.dump((1, ), file)
            Rectangle.load_from_file_csv()
            self.assertEqual(result, [])

        with open(filename, "w") as file:
            json.dump({"a": 1}, file)
            Rectangle.load_from_file_csv()
            self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
