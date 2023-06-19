#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertAlmostEqual(max_integer([5, 4, 3]), 9)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([True, False]), True)
        self.assertAlmostEqual(max_integer(), None)
        self.assertAlmostEqual(max_integer([9]), 9)
    def test_values(self):
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, {1, 2, 3})
        self.assertRaises(TypeError, max_integer, [2, None, 1])
