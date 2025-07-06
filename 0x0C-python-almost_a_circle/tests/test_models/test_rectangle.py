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
        self.assertEqual(rec.id, 9)

    def test_widthTypeErrorStr(self):
        """Test if TypeError is raised for width as string"""
        with self.assertRaises(TypeError):
            rec = Rectangle("1", 2)

    def test_widthTypeErrorNone(self):
        """Test if TypeError is raised for width as None"""
        with self.assertRaises(TypeError):
            rec = Rectangle(None, 2)

    def test_widthTypeErrorList(self):
        """Test if TypeError is raised for width as list"""
        with self.assertRaises(TypeError):
            rec = Rectangle([1, 2])

    def test_widthTypeErrorBoolean(self):
        """Test if TypeError is raised for width as boolean"""
        with self.assertRaises(TypeError):
            rec = Rectangle(True, 2)

    def test_widthTypeErrorDict(self):
        """Test if TypeError is raised for width as a dict"""
        with self.assertRaises(TypeError):
            rec = Rectangle({"width": 1}, 2)

    def test_widthTypeErrorFloat(self):
        """Test if TypeError is raised for width as a float"""
        with self.assertRaises(TypeError):
            rec = Rectangle(2.4, 3)

    def test_heightTypeErrorString(self):
        """Test if TypeError is raised for height as a string"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, "2")

    def test_heightTypeErrorNone(self):
        """Test if TypeError is raised for height as None"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, None)

    def test_heightTypeErrorList(self):
        """Test if TypeError is raised for height as a list"""
        with self.assertRaises(TypeError):
            rec = Rectangle([1, 2])

    def test_heightTypeErrorBool(self):
        """Test if TypeError is raised for height as a boolean"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, True)

    def test_heightTypeErrorDict(self):
        """Test if TypeError is raised for height as a dict"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, {"height": 2})

    def test_heightTypeErrorFloat(self):
        """Test if TypeError is raised for height as a float"""
        with self.assertRaises(TypeError):
            rec = Rectangle(2, 5.6)

    def test_xTypeErrorStr(self):
        """Test if TypeError is raised for x as a string"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, 2, "1", 0)

    def test_xTypeErrorBool(self):
        """Test if TypeError is raised for x as a boolean"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, 2, False, 0)
            rec = Rectangle(1, 2, [9], 0)
            rec = Rectangle(1, 2, 1.2, 0)
            rec = Rectangle(1, 2, None, 0)

    def test_yTypeErrorstr(self):
        """Test if TypeError is raised for y as string"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, 2, 2, "1")

    def test_yTypeErrorbool(self):
        """Test if TypeError is raised for y as boolean"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, 2, 2, False)

    def test_yTypeErrorlist(self):
        """Test if TypeError is raised for y as list"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, 2, 3, [9])

    def test_yTypeError(self):
        """Test if TypeError is raised for y as float"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, 2, 7, 1.2)

    def test_yTypeError(self):
        """Test if TypeError is raised for y as None"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1, 2, 6, None)
            
            
    def test_widthValuerror(self):
        """Test ValueError for negative width"""
        with self.assertRaises(ValueError):
            rec = Rectangle(-1, 2)
            rec = Rectangle(0, 3)

    def test_heightValuerror(self):
        """Test ValueError for negative width"""
        with self.assertRaises(ValueError):
            rec = Rectangle(1, -2)
            rec = Rectangle(3, 0)

    def test_xValuerror(self):
        """Test ValueError for negative x"""
        with self.assertRaises(ValueError):
            rec = Rectangle(1, 2, -6, 2)

    def test_yValuerror(self):
        """Test ValueError for negative """
        with self.assertRaises(ValueError):
            rec = Rectangle(1, 2, 6, -2)

    def test_argsUpdateMethod(self):
        rec = Rectangle(1, 2, 3, 4)
        rec.update(4, 5, 6, 7, 8)
        self.assertEqual(rec.id, 4)
        self.assertEqual(rec.width, 5)
        self.assertEqual(rec.height, 6)
        self.assertEqual(rec.x, 7)
        self.assertEqual(rec.y, 8)

    """
    def test_kwargsUpdateMethod(self):
        rec = Rectangle(1, 2, 3, 4, 5)
        rec.update(6, 5, {"width": 4}, {"height": 6})
        self.assertEqual(rec.width, 5)
    """
