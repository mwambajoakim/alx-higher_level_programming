#!/usr/bin/python3
"""Defines a square and returns its area"""


class Square:
    """Creates a square

        Args:
            size (int): ize of the square

        Return:
            area (int): Area of the square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of a square

            Return:
                Area (int): Area of a square
        """
        return self.__size * self.__size
