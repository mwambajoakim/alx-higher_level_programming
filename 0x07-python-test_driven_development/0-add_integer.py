#!/usr/bin/python3
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

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        int_a = int(a)
    if isinstance(b, float):
        int_b = int(b)
    return (int_a + int_b)
