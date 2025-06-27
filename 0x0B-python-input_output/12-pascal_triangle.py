#!/usr/bin/python3
"""Generate Pascal's triangle"""


def pascal_triangle(n):
    """Return a list of lists of n

        Args:
            n: Number of rows

        Return:
            A list of lists
    """
    pasc = []

    for row in range(n):
        arr = []
        for j in range(row + 1):
            if j == 0 or row == j:
                arr.append(1)
            else:
                arr.append(pasc[row - 1][j - 1] + pasc[row - 1][j])
        pasc.append(arr)
    return pasc
