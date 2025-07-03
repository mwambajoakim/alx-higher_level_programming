#!/usr/bin/python3
"""Creates a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Returns a square that inherits from Rectangle

        Args:
            size: size of the square
            x: horizontal justification
            y: vertical justification
            id: ID of the instance
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        a = self.id
        b = self.x
        c = self.y
        d = self.size
        return f"[Square] ({a}) {b}/{c} - {d}"

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.size = value
