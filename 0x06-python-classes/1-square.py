#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Creates a square

        Args:
            size (int): Size of the square

        Returns:
            A square and its size
    """
    def __init__(self, size):
        self.__size = size
