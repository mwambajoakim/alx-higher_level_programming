#!/usr/bin/python3
"""Defines a square and returns the area"""


class Square:
    """Creates a square and returns the area

        Args:
            size (int): Size of the square

        Returns:
            area (int): Area of the square
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Gets the size of a square/
        sets the value to size

            Args:
                value (int): Size of the square

            Return:
                size (int): The value of the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of a square

            Returns:
                area (int): Area of a square
        """
        return self.__size * self.__size
