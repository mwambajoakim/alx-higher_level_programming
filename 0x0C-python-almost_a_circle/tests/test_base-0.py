#!/usr/bin/python3
"""Test Base class"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ..models.base import Base
import unittest


class TestBase(unittest.TestCase):
    def test_id_None(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
    def test_with_ID(self):
        b1 = Base(4)
        self.assertEqual(b1.id, 4)
    def test_increment(self):
        b1 = Base()
        self.assertEqual(b1.id, 2)
