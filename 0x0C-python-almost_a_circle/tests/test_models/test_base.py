#!/usr/bin/python3

"""
Contains BaseTest class
"""


import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """ Testing Base Class """
    def test_initialization(self):
        """ check if Base is properly initialized """
        base = Base()
        self.assertGreater(base.id, 0)
        base = Base(10)
        self.assertEqual(base.id, 10)

    def test_assignment_to_id_when_value_is_none(self):
        """ check if Base is properly initialized """
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        base3 = Base()
        self.assertEqual(base3.id, 3)

    def test_assignment_to_id_when_value_is_int(self):
        """ check if Base is properly initialized """
        base1 = Base(5)
        self.assertEqual(base1.id, 5)
        base2 = Base(15)
        self.assertEqual(base2.id, 15)

