#!/usr/bin/python3

"""
Contains RectangleTest class
"""


import sys
from io import StringIO
import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """ Testing Rectangle Class """
    def test_cannot_initialize_with_zero_arguments(self):
        """ check if Rectangle is properly initialized """
        with self.assertRaises(TypeError) as ctx:
            Rectangle()

    def test_cannot_initialize_with_one_argument(self):
        """ check if Rectangle is properly initialized """
        with self.assertRaises(TypeError) as ctx:
            Rectangle(1)

    def test_can_initialize_with_invalid_value_for_an_argument(self):
        """ check if Rectangle is properly initialized """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle("1", 2, 3, 4)

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, "2", 3, 4)

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 2, "3", 4)

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 2, 3, "4")

        with self.assertRaises(ValueError) as ctx:
            rectangle = Rectangle(-1, 2, 3, 4)

        with self.assertRaises(ValueError) as ctx:
            rectangle = Rectangle(1, -2, 3, 4)

        with self.assertRaises(ValueError) as ctx:
            rectangle = Rectangle(1, 2, -3, 4)

        with self.assertRaises(ValueError) as ctx:
            rectangle = Rectangle(1, 2, 3, -4)

    def test_can_initialize_with_more_that_five_argument(self):
        """ check if Rectangle is properly initialized """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 2, 3, 4, 5, 6)

    def test_can_initialize_with_two_or_more_arguments(self):
        """ check if Rectangle is properly initialized """
        rectangle = Rectangle(1, 2, id=10)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)
        self.assertEqual(rectangle.id, 10)

    # setter and getter for width -------------------------------
    def test_setting_and_getting_width(self):
        """
        check if Rectangle's width instance variable can be set and got
        """

        rectangle = Rectangle(1, 2)
        self.assertEqual(rectangle.width, 1)
        rectangle.width = 5
        self.assertEqual(rectangle.width, 5)

    def test_cannot_set_width_with_a_string(self):
        """ test dealing the setting of width with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle("1", 2)
        self.assertEqual(str(ctx.exception), "width must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.width = "1"
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_cannot_set_width_with_a_bool(self):
        """ test dealing the setting of width with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(True, 2)
        self.assertEqual(str(ctx.exception), "width must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.width = True
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_cannot_set_width_with_a_float(self):
        """ test dealing the setting of width with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1.1, 2)
        self.assertEqual(str(ctx.exception), "width must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.width = 1.1
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_cannot_set_width_with_none(self):
        """ test dealing the setting of width with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(None, 2)
        self.assertEqual(str(ctx.exception), "width must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.width = None
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_cannot_set_width_with_a_list(self):
        """ test dealing the setting of width with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle([1, 2], 2)
        self.assertEqual(str(ctx.exception), "width must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.width = [1, 2]
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_cannot_set_width_with_a_tuple(self):
        """ test dealing the setting of width with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle((1, 1), 2)
        self.assertEqual(str(ctx.exception), "width must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.width = (1, 1)
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_cannot_set_width_with_a_dict(self):
        """ test dealing the setting of width with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle({"a": 1.1}, 2)
        self.assertEqual(str(ctx.exception), "width must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.width = {"a": 1.1}
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_cannot_set_width_with_a_set(self):
        """ test dealing the setting of width with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle({1, 2}, 2)
        self.assertEqual(str(ctx.exception), "width must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.width = {1, 2}
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_cannot_set_width_with_a_frozenset(self):
        """ test dealing the setting of width with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(frozenset({1, 2}), 2)
        self.assertEqual(str(ctx.exception), "width must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.width = frozenset({1, 2})
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_cannot_set_width_with_a_negative_number(self):
        """ test dealing with setting width with to int less or equal to 0 """

        with self.assertRaises(ValueError) as ctx:
            rectangle = Rectangle(-1, 2)
        self.assertEqual(str(ctx.exception), "width must be > 0")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(ValueError) as ctx:
            rectangle.width = -1
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_cannot_set_width_with_zero(self):
        """ test dealing with setting width with to int less or equal to 0 """

        with self.assertRaises(ValueError) as ctx:
            rectangle = Rectangle(0, 2)
        self.assertEqual(str(ctx.exception), "width must be > 0")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(ValueError) as ctx:
            rectangle.width = 0
        self.assertEqual(str(ctx.exception), "width must be > 0")

    # setter and getter for height --------------------------------------

    def test_setting_and_getting_height(self):
        """
        check if Rectangle's height instance variable can be set and got
        """

        rectangle = Rectangle(1, 2)
        self.assertEqual(rectangle.height, 2)
        rectangle.height = 5
        self.assertEqual(rectangle.height, 5)

    def test_cannot_set_height_with_a_string(self):
        """ test dealing the setting of height with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, "2")
        self.assertEqual(str(ctx.exception), "height must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.height = "2"
        self.assertEqual(str(ctx.exception), "height must be an integer")

    def test_cannot_set_height_with_a_bool(self):
        """ test dealing the setting of height with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, True, 2)
        self.assertEqual(str(ctx.exception), "height must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.height = True
        self.assertEqual(str(ctx.exception), "height must be an integer")

    def test_cannot_set_height_with_a_float(self):
        """ test dealing the setting of height with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 2.1)
        self.assertEqual(str(ctx.exception), "height must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.height = 2.1
        self.assertEqual(str(ctx.exception), "height must be an integer")

    def test_cannot_set_height_with_none(self):
        """ test dealing the setting of height with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, None, 2)
        self.assertEqual(str(ctx.exception), "height must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.height = None
        self.assertEqual(str(ctx.exception), "height must be an integer")

    def test_cannot_set_height_with_a_list(self):
        """ test dealing the setting of height with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, [1, 2], 2)
        self.assertEqual(str(ctx.exception), "height must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.height = [1, 2]
        self.assertEqual(str(ctx.exception), "height must be an integer")

    def test_cannot_set_height_with_a_tuple(self):
        """ test dealing the setting of height with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, (1, 1), 2)
        self.assertEqual(str(ctx.exception), "height must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.height = (1, 1)
        self.assertEqual(str(ctx.exception), "height must be an integer")

    def test_cannot_set_height_with_a_dict(self):
        """ test dealing the setting of height with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, {"a": 1.1}, 2)
        self.assertEqual(str(ctx.exception), "height must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.height = {"a": 1.1}
        self.assertEqual(str(ctx.exception), "height must be an integer")

    def test_cannot_set_height_with_a_set(self):
        """ test dealing the setting of height with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, {1, 2}, 2)
        self.assertEqual(str(ctx.exception), "height must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.height = {1, 2}
        self.assertEqual(str(ctx.exception), "height must be an integer")

    def test_cannot_set_height_with_a_frozenset(self):
        """ test dealing the setting of height with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, frozenset({1, 2}), 2)
        self.assertEqual(str(ctx.exception), "height must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.height = frozenset({1, 2})
        self.assertEqual(str(ctx.exception), "height must be an integer")

    def test_cannot_set_height_with_a_negative_number(self):
        """ test dealing with setting height with to int less or equal to 0 """

        with self.assertRaises(ValueError) as ctx:
            rectangle = Rectangle(1, -1, 2)
        self.assertEqual(str(ctx.exception), "height must be > 0")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(ValueError) as ctx:
            rectangle.height = -1
        self.assertEqual(str(ctx.exception), "height must be > 0")

    def test_cannot_set_height_with_zero(self):
        """ test dealing with setting height with to int less or equal to 0 """

        with self.assertRaises(ValueError) as ctx:
            rectangle = Rectangle(1, 0, 2)
        self.assertEqual(str(ctx.exception), "height must be > 0")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(ValueError) as ctx:
            rectangle.height = 0
        self.assertEqual(str(ctx.exception), "height must be > 0")

    # setter and getter for x --------------------------------------

    def test_setting_and_getting_x(self):
        """
        check if Rectangle's x instance variable can be set and got
        """

        rectangle = Rectangle(1, 2)
        self.assertEqual(rectangle.x, 0)
        rectangle.x = 5
        self.assertEqual(rectangle.x, 5)

    def test_cannot_set_x_with_a_string(self):
        """ test dealing the setting of x with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 2, "2")
        self.assertEqual(str(ctx.exception), "x must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.x = "2"
        self.assertEqual(str(ctx.exception), "x must be an integer")

    def test_cannot_set_x_with_a_bool(self):
        """ test dealing the setting of x with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 2, True, 2)
        self.assertEqual(str(ctx.exception), "x must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.x = True
        self.assertEqual(str(ctx.exception), "x must be an integer")

    def test_cannot_set_x_with_a_float(self):
        """ test dealing the setting of x with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 2, 2.1)
        self.assertEqual(str(ctx.exception), "x must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.x = 2.1
        self.assertEqual(str(ctx.exception), "x must be an integer")

    def test_cannot_set_x_with_none(self):
        """ test dealing the setting of x with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 2, None, 2)
        self.assertEqual(str(ctx.exception), "x must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.x = None
        self.assertEqual(str(ctx.exception), "x must be an integer")

    def test_cannot_set_x_with_a_list(self):
        """ test dealing the setting of x with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 2, [1, 2], 2)
        self.assertEqual(str(ctx.exception), "x must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.x = [1, 2]
        self.assertEqual(str(ctx.exception), "x must be an integer")

    def test_cannot_set_x_with_a_tuple(self):
        """ test dealing the setting of x with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 2, (1, 1), 2)
        self.assertEqual(str(ctx.exception), "x must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.x = (1, 1)
        self.assertEqual(str(ctx.exception), "x must be an integer")

    def test_cannot_set_x_with_a_dict(self):
        """ test dealing the setting of x with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 2, {"a": 1.1}, 2)
        self.assertEqual(str(ctx.exception), "x must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.x = {"a": 1.1}
        self.assertEqual(str(ctx.exception), "x must be an integer")

    def test_cannot_set_x_with_a_set(self):
        """ test dealing the setting of x with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 1, {1, 2}, 2)
        self.assertEqual(str(ctx.exception), "x must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.x = {1, 2}
        self.assertEqual(str(ctx.exception), "x must be an integer")

    def test_cannot_set_x_with_a_frozenset(self):
        """ test dealing the setting of x with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 1, frozenset({1, 2}), 2)
        self.assertEqual(str(ctx.exception), "x must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.x = frozenset({1, 2})
        self.assertEqual(str(ctx.exception), "x must be an integer")

    def test_cannot_set_x_with_a_negative_number(self):
        """ test dealing with setting x with to int less or equal to 0 """

        with self.assertRaises(ValueError) as ctx:
            rectangle = Rectangle(1, 1, -1, 2)
        self.assertEqual(str(ctx.exception), "x must be >= 0")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(ValueError) as ctx:
            rectangle.x = -1
        self.assertEqual(str(ctx.exception), "x must be >= 0")

    def test_cannot_set_x_with_zero(self):
        """ test dealing with setting x with to int less or equal to 0 """

        rectangle = Rectangle(1, 1, 0, 1)
        self.assertEqual(rectangle.x, 0)

        rectangle = Rectangle(1, 2, 2, 2)
        rectangle.x = 0
        self.assertEqual(rectangle.x, 0)

    # setter and getter for y --------------------------------------

    def test_setting_and_getting_y(self):
        """
        check if Rectangle's y instance variable can be set and got
        """

        rectangle = Rectangle(1, 2)
        self.assertEqual(rectangle.y, 0)
        rectangle.y = 5
        self.assertEqual(rectangle.y, 5)

    def test_cannot_set_y_with_a_string(self):
        """ test dealing the setting of y with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 1, 1, "2")
        self.assertEqual(str(ctx.exception), "y must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.y = "2"
        self.assertEqual(str(ctx.exception), "y must be an integer")

    def test_cannot_set_y_with_a_bool(self):
        """ test dealing the setting of y with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 1, 1, True, 2)
        self.assertEqual(str(ctx.exception), "y must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.y = True
        self.assertEqual(str(ctx.exception), "y must be an integer")

    def test_cannot_set_y_with_a_float(self):
        """ test dealing the setting of y with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 1, 1, 2.1)
        self.assertEqual(str(ctx.exception), "y must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.y = 2.1
        self.assertEqual(str(ctx.exception), "y must be an integer")

    def test_cannot_set_y_with_none(self):
        """ test dealing the setting of y with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 1, 1, None, 2)
        self.assertEqual(str(ctx.exception), "y must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.y = None
        self.assertEqual(str(ctx.exception), "y must be an integer")

    def test_cannot_set_y_with_a_list(self):
        """ test dealing the setting of y with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 1, 1, [1, 2], 2)
        self.assertEqual(str(ctx.exception), "y must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.y = [1, 2]
        self.assertEqual(str(ctx.exception), "y must be an integer")

    def test_cannot_set_y_with_a_tuple(self):
        """ test dealing the setting of y with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 1, 1, (1, 1), 2)
        self.assertEqual(str(ctx.exception), "y must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.y = (1, 1)
        self.assertEqual(str(ctx.exception), "y must be an integer")

    def test_cannot_set_y_with_a_dict(self):
        """ test dealing the setting of y with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 1, 1, {"a": 1.1}, 2)
        self.assertEqual(str(ctx.exception), "y must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.y = {"a": 1.1}
        self.assertEqual(str(ctx.exception), "y must be an integer")

    def test_cannot_set_y_with_a_set(self):
        """ test dealing the setting of y with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 1, 1, {1, 2}, 2)
        self.assertEqual(str(ctx.exception), "y must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.y = {1, 2}
        self.assertEqual(str(ctx.exception), "y must be an integer")

    def test_cannot_set_y_with_a_frozenset(self):
        """ test dealing the setting of y with non int """

        with self.assertRaises(TypeError) as ctx:
            rectangle = Rectangle(1, 1, 1, frozenset({1, 2}), 2)
        self.assertEqual(str(ctx.exception), "y must be an integer")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError) as ctx:
            rectangle.y = frozenset({1, 2})
        self.assertEqual(str(ctx.exception), "y must be an integer")

    def test_cannot_set_y_with_a_negative_number(self):
        """ test dealing with setting y with to int less or equal to 0 """

        with self.assertRaises(ValueError) as ctx:
            rectangle = Rectangle(1, 1, 1, -1, 2)
        self.assertEqual(str(ctx.exception), "y must be >= 0")

        rectangle = Rectangle(1, 2)
        with self.assertRaises(ValueError) as ctx:
            rectangle.y = -1
        self.assertEqual(str(ctx.exception), "y must be >= 0")

    def test_cannot_set_y_with_zero(self):
        """ test dealing with setting y with to int less or equal to 0 """

        rectangle = Rectangle(1, 1, 1, 0)
        self.assertEqual(rectangle.y, 0)

        rectangle = Rectangle(1, 2, 2, 2)
        rectangle.y = 0
        self.assertEqual(rectangle.y, 0)

    # area --------------------------------------

    def test_cannot_calculate_area_when_method_is_called_with_arguments(self):
        """ test the area method of an instance """

        with self.assertRaises(TypeError) as ctx:
            r1 = Rectangle(3, 2)
            r1.area(1)

    def test_can_calculate_area(self):
        """ test the area method of an instance """

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 3 * 2)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 2 * 10)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 8 * 7)

    # display --------------------------------------

    def test_cannot_display_when_method_is_called_with_arguments(self):
        """ test the display method of an instance """

        with self.assertRaises(TypeError) as ctx:
            r1 = Rectangle(3, 2)
            r1.display(1)

    def test_rectangle_can_be_displayed_without_x_and_y(self):
        """ test the area method of an instance """

        captured = StringIO()
        sys.stdout = captured

        r1 = Rectangle(4, 6)
        r1.display()
        self.assertEqual(captured.getvalue(),
                         "####\n####\n####\n####\n####\n####\n")

        captured = StringIO()
        sys.stdout = captured

        r1 = Rectangle(2, 2)
        r1.display()
        self.assertEqual(captured.getvalue(), "##\n##\n")
        sys.stdout = sys.__stdout__

    def test_rectangle_can_be_displayed_with_x_and_y(self):
        """ test the area method of an instance """

        captured = StringIO()
        sys.stdout = captured

        r1 = Rectangle(4, 6, 1, 2)
        r1.display()
        self.assertEqual(captured.getvalue(),
                         "\n\n ####\n ####\n ####\n ####\n ####\n ####\n")

        captured = StringIO()
        sys.stdout = captured

        r1 = Rectangle(2, 2, 2, 1)
        r1.display()
        self.assertEqual(captured.getvalue(), "\n  ##\n  ##\n")

        captured = StringIO()
        sys.stdout = captured

        r1 = Rectangle(2, 2, 0, 2)
        r1.display()
        self.assertEqual(captured.getvalue(), "\n\n##\n##\n")

        captured = StringIO()
        sys.stdout = captured

        r1 = Rectangle(2, 2, 2, 0)
        r1.display()
        self.assertEqual(captured.getvalue(), "  ##\n  ##\n")

        sys.stdout = sys.__stdout__

    # __str__ implementation --------------------------------------

    def test__can_get_string_representation(self):
        """ test the area method of an instance """

        r1 = Rectangle(4, 6)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 0/0 - 4/6")

    # update ------------------------------------

    def test_can_call_update_with_no_arguments(self):
        """ testing update instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update()
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def test_can_call_update_with_more_than_one_arguments(self):
        """ testing update instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_can_call_update_with_one_arguments(self):
        """ testing update instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def test_can_call_update_with_two_arguments(self):
        """ testing update instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(1, 2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def test_can_call_update_with_three_arguments(self):
        """ testing update instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(1, 2, 3)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def test_can_call_update_with_four_arguments(self):
        """ testing update instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(1, 2, 3, 4)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 10)

    def test_can_call_update_with_five_arguments(self):
        """ testing update instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_cannot_call_update_with_invalid_positional_argument_value(self):
        """ testing update instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        with self.assertRaises(TypeError) as ctx:
            r.update("the id", "1", 2)

    def test_can_call_update_with_more_than_one_named_arguments(self):
        """ testing update instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(id=1, width=2, height=3, x=4, y=5, a=6, b=7)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_can_call_update_with_id_named_arguments(self):
        """ testing update instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(id=1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def test_can_call_update_with_width_named_arguments(self):
        """ testing update instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(width=1)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def test_can_call_update_with_height_named_arguments(self):
        """ testing update instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(height=1)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def test_can_call_update_with_x_named_arguments(self):
        """ testing update instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(x=1)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 10)

    def test_can_call_update_with_y_named_arguments(self):
        """ testing update instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(y=1)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 1)

    def test_can_call_update_with_two_named_arguments(self):
        """ testing update instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(x=1, id=2)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 10)

    def test_can_call_update_with_three_named_arguments(self):
        """ testing update instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(x=1, width=2, id=3)
        self.assertEqual(r.id, 3)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 10)

    def test_can_call_update_with_four_named_arguments(self):
        """ testing update instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(x=1, y=2, width=3, height=4)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_can_call_update_with_five_arguments(self):
        """ testing update instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(y=1, x=2, height=3, width=4, id=5)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)

    def test_can_call_update_with_positional_before_named_arguments(self):
        """ testing update instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(5, 4, y=1, x=2, height=3)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)

    def test_cannot_call_update_with_invalid_named_argument_value(self):
        """ testing update instance method """

        r = Rectangle(10, 10, 10, 10, 10)
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

        r = Rectangle(10, 10, 10, 10, 10)
        r_dict = r.to_dictionary()
        self.assertIsInstance(r_dict, dict)

    def test_to_dictionary_dict_has_five_keys(self):
        """ testing to_dictionary instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        r_dict = r.to_dictionary()
        self.assertEqual(len(r_dict), 5)

    def test_to_dictionary_dict_contains_only_specified_keys(self):
        """ testing to_dictionary instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        r_dict = r.to_dictionary()

        check_dict = {"id": 10, "width": 10, "height": 10, "x": 10, "y": 10}
        for key, value in check_dict.items():
            self.assertEqual(value, r_dict[key])

    def test_to_dictionary_cannot_be_called_with_arguments(self):
        """ testing to_dictionary instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        with self.assertRaises(TypeError) as ctx:
            r.to_dictionary(2)

    def test_two_or_more_rectangles_can_have_equal_dict_reps(self):
        """ testing to_dictionary instance method """

        r = Rectangle(10, 10, 10, 10, 10)
        r_dict = r.to_dictionary()

        r1 = Rectangle(1, 1, 1, 1, 1)
        r1.update(**r_dict)
        self.assertEqual(r1.to_dictionary(), r_dict)


if __name__ == "__main__":
    unittest.main()
