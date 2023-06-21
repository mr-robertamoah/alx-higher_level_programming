#!/usr/bin/python3

"""
Contains SquareTest class
"""


import sys
from io import StringIO
import unittest
from models.square import Square


class SquareTest(unittest.TestCase):
    """ Testing Square Class """
    def test_cannot_initialize_with_zero_arguments(self):
        """ check if Square is properly initialized """
        with self.assertRaises(TypeError) as ctx:
            Square()

    def test_can_initialize_with_more_that_four_argument(self):
        """ check if Square is properly initialized """

        with self.assertRaises(TypeError) as ctx:
            square = Square(1, 2, 3, 4, 5)

    def test_cannot_initialize_with_invalid_value_for_an_argument(self):
        """ check if Square is properly initialized """

        with self.assertRaises(TypeError) as ctx:
            square = Square("1", 2, 3)

        with self.assertRaises(TypeError) as ctx:
            square = Square(1, "2", 3)

        with self.assertRaises(TypeError) as ctx:
            square = Square(1, 2, "3")

        with self.assertRaises(ValueError) as ctx:
            square = Square(-1, 2, 3)

        with self.assertRaises(ValueError) as ctx:
            square = Square(1, -2, 3)

        with self.assertRaises(ValueError) as ctx:
            square = Square(1, 2, -3)

    def test_can_initialize_with_one_argument(self):
        """ check if Square is properly initialized """

        square = Square(1)
        self.assertEqual(square.width, 1)
        self.assertEqual(square.height, 1)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertGreater(square.id, 0)

    def test_can_initialize_with_two_or_more_arguments(self):
        """ check if Square is properly initialized """
        square = Square(1, 2, 10)
        self.assertEqual(square.width, 1)
        self.assertEqual(square.height, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 10)

    # __str__ implementation --------------------------------------

    def test__can_get_string_representation(self):
        """ test the area method of an instance """

        r1 = Square(4, 6)
        self.assertEqual(str(r1), f"[Square] ({r1.id}) 6/0 - 4")

    # setter and getter for size -------------------------------
    def test_setting_and_getting_size(self):
        """
        check if Square's size instance variable can be set and got
        """

        square = Square(1, 2)
        self.assertEqual(square.size, 1)
        square.size = 5
        self.assertEqual(square.size, 5)

    def test_cannot_set_size_with_a_string(self):
        """ test dealing the setting of size with non int """

        with self.assertRaises(TypeError) as ctx:
            square = Square("1", 2)
        self.assertEqual(str(ctx.exception), "width must be an integer")

        square = Square(1, 2)
        with self.assertRaises(TypeError) as ctx:
            square.size = "1"
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_cannot_set_size_with_a_bool(self):
        """ test dealing the setting of size with non int """

        with self.assertRaises(TypeError) as ctx:
            square = Square(True, 2)
        self.assertEqual(str(ctx.exception), "width must be an integer")

        square = Square(1, 2)
        with self.assertRaises(TypeError) as ctx:
            square.size = True
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_cannot_set_size_with_a_float(self):
        """ test dealing the setting of size with non int """

        with self.assertRaises(TypeError) as ctx:
            square = Square(1.1, 2)
        self.assertEqual(str(ctx.exception), "width must be an integer")

        square = Square(1, 2)
        with self.assertRaises(TypeError) as ctx:
            square.size = 1.1
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_cannot_set_size_with_none(self):
        """ test dealing the setting of size with non int """

        with self.assertRaises(TypeError) as ctx:
            square = Square(None, 2)
        self.assertEqual(str(ctx.exception), "width must be an integer")

        square = Square(1, 2)
        with self.assertRaises(TypeError) as ctx:
            square.size = None
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_cannot_set_size_with_a_list(self):
        """ test dealing the setting of size with non int """

        with self.assertRaises(TypeError) as ctx:
            square = Square([1, 2], 2)
        self.assertEqual(str(ctx.exception), "width must be an integer")

        square = Square(1, 2)
        with self.assertRaises(TypeError) as ctx:
            square.size = [1, 2]
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_cannot_set_size_with_a_tuple(self):
        """ test dealing the setting of size with non int """

        with self.assertRaises(TypeError) as ctx:
            square = Square((1, 1), 2)
        self.assertEqual(str(ctx.exception), "width must be an integer")

        square = Square(1, 2)
        with self.assertRaises(TypeError) as ctx:
            square.size = (1, 1)
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_cannot_set_size_with_a_dict(self):
        """ test dealing the setting of size with non int """

        with self.assertRaises(TypeError) as ctx:
            square = Square({"a": 1.1}, 2)
        self.assertEqual(str(ctx.exception), "width must be an integer")

        square = Square(1, 2)
        with self.assertRaises(TypeError) as ctx:
            square.size = {"a": 1.1}
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_cannot_set_size_with_a_set(self):
        """ test dealing the setting of size with non int """

        with self.assertRaises(TypeError) as ctx:
            square = Square({1, 2}, 2)
        self.assertEqual(str(ctx.exception), "width must be an integer")

        square = Square(1, 2)
        with self.assertRaises(TypeError) as ctx:
            square.size = {1, 2}
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_cannot_set_size_with_a_frozenset(self):
        """ test dealing the setting of size with non int """

        with self.assertRaises(TypeError) as ctx:
            square = Square(frozenset({1, 2}), 2)
        self.assertEqual(str(ctx.exception), "width must be an integer")

        square = Square(1, 2)
        with self.assertRaises(TypeError) as ctx:
            square.size = frozenset({1, 2})
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_cannot_set_size_with_a_negative_number(self):
        """ test dealing with setting size with to int less or equal to 0 """

        with self.assertRaises(ValueError) as ctx:
            square = Square(-1, 2)
        self.assertEqual(str(ctx.exception), "width must be > 0")

        square = Square(1, 2)
        with self.assertRaises(ValueError) as ctx:
            square.size = -1
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_cannot_set_size_with_zero(self):
        """ test dealing with setting size with to int less or equal to 0 """

        with self.assertRaises(ValueError) as ctx:
            square = Square(0, 2)
        self.assertEqual(str(ctx.exception), "width must be > 0")

        square = Square(1, 2)
        with self.assertRaises(ValueError) as ctx:
            square.size = 0
        self.assertEqual(str(ctx.exception), "width must be > 0")

    # update ------------------------------------

    def test_can_call_update_with_no_arguments(self):
        """ testing update instance method """

        r = Square(10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update()
        self.assertEqual(r.id, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def test_can_call_update_with_more_than_one_arguments(self):
        """ testing update instance method """

        r = Square(10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.size, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_can_call_update_with_one_arguments(self):
        """ testing update instance method """

        r = Square(10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def test_can_call_update_with_two_arguments(self):
        """ testing update instance method """

        r = Square(10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(1, 2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.size, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def test_can_call_update_with_three_arguments(self):
        """ testing update instance method """

        r = Square(10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(1, 2, 3)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.size, 2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 10)

    def test_can_call_update_with_four_arguments(self):
        """ testing update instance method """

        r = Square(10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(1, 2, 3, 4)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.size, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_cannot_call_update_with_invalid_positional_argument_value(self):
        """ testing update instance method """

        r = Square(10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        with self.assertRaises(TypeError) as ctx:
            r.update("the id", "1", 2)

    def test_can_call_update_with_more_than_one_named_arguments(self):
        """ testing update instance method """

        r = Square(10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(id=1, size=2, x=4, y=5, a=6, b=7)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.size, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_can_call_update_with_id_named_arguments(self):
        """ testing update instance method """

        r = Square(10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(id=1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def test_can_call_update_with_size_named_arguments(self):
        """ testing update instance method """

        r = Square(10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(size=1)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.size, 1)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def test_can_call_update_with_x_named_arguments(self):
        """ testing update instance method """

        r = Square(10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(x=1)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 10)

    def test_can_call_update_with_y_named_arguments(self):
        """ testing update instance method """

        r = Square(10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(y=1)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 1)

    def test_can_call_update_with_two_named_arguments(self):
        """ testing update instance method """

        r = Square(10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(x=1, id=2)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 10)

    def test_can_call_update_with_three_named_arguments(self):
        """ testing update instance method """

        r = Square(10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(x=1, size=2, id=3)
        self.assertEqual(r.id, 3)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.size, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 10)

    def test_can_call_update_with_four_named_arguments(self):
        """ testing update instance method """

        r = Square(10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(x=1, y=2, size=3)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.size, 3)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_can_call_update_with_five_arguments(self):
        """ testing update instance method """

        r = Square(10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(y=1, x=2, size=3, id=5)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.size, 3)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)

    def test_update_with_positional_before_ignored_named_arguments(self):
        """ testing update instance method """

        r = Square(10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(5, 4, y=1, x=2)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.size, 4)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def test_cannot_call_update_with_invalid_named_argument_value(self):
        """ testing update instance method """

        r = Square(10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        with self.assertRaises(TypeError) as ctx:
            r.update(x="1", id=2)

    # to_dictionary --------------------------------------

    def test_can_return_dictionary_rep_of_instance(self):
        """ testing to_dictionary instance method """

        r = Square(10, 10, 10, 10)
        r_dict = r.to_dictionary()
        self.assertIsInstance(r_dict, dict)

    def test_to_dictionary_dict_has_four_keys(self):
        """ testing to_dictionary instance method """

        r = Square(10, 10, 10, 10)
        r_dict = r.to_dictionary()
        self.assertEqual(len(r_dict), 4)

    def test_to_dictionary_dict_contains_only_specified_keys(self):
        """ testing to_dictionary instance method """

        r = Square(10, 10, 10, 10)
        r_dict = r.to_dictionary()

        check_dict = {"id": 10, "size": 10, "x": 10, "y": 10}
        for key, value in check_dict.items():
            self.assertEqual(value, r_dict[key])

    def test_to_dictionary_cannot_be_called_with_arguments(self):
        """ testing to_dictionary instance method """

        r = Square(10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        with self.assertRaises(TypeError) as ctx:
            r.to_dictionary(2)

    def test_two_or_more_rectangles_can_have_equal_dict_reps(self):
        """ testing to_dictionary instance method """

        r = Square(10, 10, 10, 10)
        r_dict = r.to_dictionary()

        r1 = Square(1, 1, 1, 1)
        r1.update(**r_dict)
        self.assertEqual(r1.to_dictionary(), r_dict)


if __name__ == "__main__":
    unittest.main()
