#!/usr/bin/python3
"""Test the Rectangle class"""
import os
import sys
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """Test each attribute of Rectangle"""
    def test_dimensions(self):
        """Test the dimensions"""
        rec = Rectangle(1, 2)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)

    def test_inherits_from_Base(self):
        """Test Rectangle inherits from Base"""
        rec = Rectangle(1, 1)
        self.assertEqual(rec.id, 6)

    def test_widthTypeError(self):
        """Test if TypeError is raised for width non int"""
        with self.assertRaises(TypeError):
            rec = Rectangle("1", 2)
            rec = Rectangle(None, 2)
            rec = Rectangle([1, 2])
            rec = Rectangle(True, 2)
            rec = Rectangle({"width": 1}, 2)
            rec = Rectangle(2.4, 3)

    def test_heightTypeError(self):
        """Test if TypeError is raised for height non int"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, "2")
            rec = Rectangle(1, None)
            rec = Rectangle([1, 2])
            rec = Rectangle(1, True)
            rec = Rectangle(1, {"height": 2})
            rec = Rectangle(2, 5.6)

    def test_widthValuerror(self):
        """Test ValueError for negative width"""
        with self.assertRaises(ValueError):
            rec = Rectangle(-1, 2)

    def test_heightValuerror(self):
        """Test ValueError for negative width"""
        with self.assertRaises(ValueError):
            rec = Rectangle(1, -2)
