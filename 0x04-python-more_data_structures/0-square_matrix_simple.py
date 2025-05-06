#!/usr/bin/python3
def square_matrix_simple(matrix=[[]]):
    """Computes square value of elements in matrix

        Args:
            matrix: matrix list of elements

        Return:
        list matrix of squares
    """
    return [[num ** 2 for num in row]for row in matrix]
