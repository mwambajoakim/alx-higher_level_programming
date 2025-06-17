#!/usr/bin/python3
"""Tests a function that determines lergest memeber of list"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests every part of function max_integer"""

    def test_positiveIntegers(self):
        """Test a list with positive integers"""
        number = max_integer([2, 5, 8])
        self.assertEqual(number, 8)

    def test_negativeIintegers(self):
        """Test a list with negative integers"""
        number_negative = max_integer([-2, -5, -8])
        self.assertEqual(number_negative, -2)

    def test_mixedIntegers(self):
        """Test a list with both positive and negative integers"""
        mixed_nums = max_integer([1, 37, -97, 97, -37, -1])
        self.assertEqual(mixed_nums, 97)

    def test_emptyList(self):
        """Test an empty list"""
        empty = max_integer([])
        self.assertIsNone(empty)
        self.assertFalse(empty)

    def test_sortedList(self):
        """Test a sorted list"""
        sorted = max_integer([2, 4, 6, 9, 13, 15, 28])
        self.assertEqual(sorted, 28)

    def test_similarInteger(self):
        """Test a list with the same number"""
        similar = max_integer([90, 90, 90])
        self.assertEqual(similar, 90)

    def test_floatNumber(self):
        """Test float numbers"""
        flt = max_integer([2, 7.5, 9, 6.3, 4, 6, 20.6])
        self.assertEqual(flt, 20.6)

    def test_singleElement(self):
        single = max_integer([9])
        self.assertEqual(single, 9)
