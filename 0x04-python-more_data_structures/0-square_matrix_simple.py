#!/usr/bin/python3
def square_matrix_simple(matrix=[[]]):
    """Computes square value of elements in matrix

        Args:
            matrix: matrix list of elements

        Return:
        list matrix of squares
    """
    new_matrix = []
    new = 1
    for row in matrix:
        for num in row:
            new = num ** 2
            new_matrix.append(new)
    return new_matrix
