#!/usr/bin/python3
"""Defines a square and its area"""


class Square:
    """Creates a square and returns the area

        Args:
            size (int): The size of the square

        Return:
            area (int): Area of the square
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Sets and gets the value for size

            Args:
                value (int): value for square size

            Return:
                size (int): Sets the size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of square

            Return:
                area (int): Area of a square
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints square to stdout"""
        if self.__size == 0:
            print()
        for i in range(1, self.__size + 1):
            for j in range(1, self.__size + 1):
                print("{}".format("#"), end="")
            print()
