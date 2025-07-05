#!/usr/bin/python3
"""Tests the class Square"""
import os
import sys
from models.square import Square
import unittest

class TestSquare(unittest.TestCase):

	def testSize(self):
		sq = Square(3)
		self.assertEqual(sq.size, 3)
		self.assertEqual(sq.id, 2)

	def testID(self):
		sq = Square(2, 6)
		self.assertEqual(sq.id, 1)

	def testAssignedId(self):
		sq = Square(2, 0, 0, 12)
		self.assertEqual(sq.id, 12)

	def testSizeTypeError(self):
		with self.assertRaises(TypeError):
			sq = Square("3")
			sq = Square([8])

	def testSizeValueError(self):
		with self.assertRaises(ValueError):
			sq = Square(0)
			sq = Square(-4)
