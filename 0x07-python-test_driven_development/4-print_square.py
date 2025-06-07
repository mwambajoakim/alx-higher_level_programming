#!/usr/bin/python3
"""This module prints a square"""


def print_square(size):
    """Prints a square of length size

        Args:
            size: Length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for row in range(size):
        for i in range(size):
            print("{}".format("#"), end="")
        print()
    print()
