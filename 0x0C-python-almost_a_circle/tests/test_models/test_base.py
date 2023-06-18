#!/usr/bin/python3

"""
Contains BaseTest class
"""


import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """ Testing Base Class """
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

if __name__ == "__main__":
    unittest.main()
