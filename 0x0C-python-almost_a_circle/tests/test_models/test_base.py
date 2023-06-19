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
        paths = ["Base.json", "Rectangle.json", "Square.json"]
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

    def test_to_json_string_returns_none_when_called_with_neither_list_nor_none(self):
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
        self.assertEqual(json_string, Rectangle.to_json_string([r.to_dictionary()]))
        self.assertEqual(json_string, Square.to_json_string([r.to_dictionary()]))

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

    def test_can_save_when_save_to_file_is_called_with_empty_list(self):
        """ testing save_to_file class method """

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

    def test_calling_save_to_file_with_more_than_one_argument(self):
        """ testing save_to_file class method """

        with self.assertRaises(TypeError) as ctx:
            Base.save_to_file([], [])

    def test_the_use_of_one_base_object_list_as_argument(self):
        """ testing save_to_file class method """

        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), json.dumps([r.to_dictionary()]))

    def test_the_use_of_multiple_same_base_object_list_as_argument(self):
        """ testing save_to_file class method """

        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), json.dumps([
							 r1.to_dictionary(),
                                                         r2.to_dictionary()
                                                     ]))

    def test_the_use_of_multiple_same_base_object_list_as_argument(self):
        """ testing save_to_file class method """

        r1 = Rectangle(1, 2)
        r2 = Square(3, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), json.dumps([
							 r1.to_dictionary(),
                                                         r2.to_dictionary()
                                                     ]))

    def test_the_use_of_multiple_different_base_object_list_as_argument(self):
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

if __name__ == "__main__":
    unittest.main()
