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
    int_a = a
    int_b = b

    if a is None or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if b is None or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        int_a = int(a)
    if isinstance(b, float):
        int_b = int(b)
    return (int_a + int_b)
