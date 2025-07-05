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