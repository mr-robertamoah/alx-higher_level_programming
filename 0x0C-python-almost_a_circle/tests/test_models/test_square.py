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

    def test_can_initialize_with_invalid_value_for_an_argument(self):
        """ check if Square is properly initialized """

        with self.assertRaises(TypeError) as ctx:
            square = Square("1", 2, 3)

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

    # setter and getter for with -------------------------------

    # --------------------------------------

if __name__ == "__main__":
    unittest.main()
