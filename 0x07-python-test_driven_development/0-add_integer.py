#!/usr/bin/python3
"""This is the path to python"""


def add_integer(a, b=98):
    """Adds two integers

        Args:
            a: First integer
            b: Second integer

        Return:
            Sum of a and b
    """
    if a is None or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if b is None or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
