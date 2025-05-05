#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples.

        Args:
            tuple_a: First tuple.
            tuple_b: Second tuple.

        Return:
            Tuple with two integers
    """
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = (0, 0,)
        else:
            tuple_a += (0,)
    if len(tuple_b) < 2 or len(tuple_b) == 0:
        if len(tuple_b) == 0:
            tuple_b = (0, 0,)
        else:
            tuple_b += (0,)
    c = tuple_a[0] + tuple_b[0]
    d = tuple_a[1] + tuple_b[1]
    e = (c, d)

    return e
