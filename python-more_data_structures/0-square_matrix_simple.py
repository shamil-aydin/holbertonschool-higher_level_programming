#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix."""
    if matrix is None:
        return None
    return [[col ** 2 for col in row] for row in matrix]
