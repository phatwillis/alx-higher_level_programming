#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([2, 4, 6.6, 8, 10]), 10)
        self.assertEqual(max_integer([]), None)

    def test_strings(self):
        self.assertEqual(max_integer('abcd'), 'd')
        self.assertEqual(max_integer(''), None)

if __name__ == '__main__':
    unittest.main()
