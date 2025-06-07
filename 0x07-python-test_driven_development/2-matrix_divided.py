#!/usr/bin/python3
"""This module divides a matrix by a number"""


def matrix_divided(matrix, div):
    """Divides elemnts of a matrix by a number

        Args:
            matrix: A list of elements in a matrix
            div: Number to divide by

        Returns:
            A new matrix with elements divided by div
    """
    row_length = len(matrix[0])
    new_matrix = []
    new_row = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                 "integers/floats")
            new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)
        new_row = []
    return new_matrix

