#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    TestCase Inherited class to run tests on the max_integer function

    """

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer("abc"), "c")
        self.assertEqual(max_integer([1,3, 4, 2]), 4)
        self.assertEqual(max_integer([]), None)
        with self.assertRaises(TypeError):
            max_integer([1, (1, 2), 3])
        with self.assertRaises(TypeError):
            max_integer([1, "abc", 3])
        with self.assertRaises(TypeError):
            max_integer(1)

