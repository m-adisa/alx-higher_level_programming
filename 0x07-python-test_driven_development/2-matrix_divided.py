#!/usr/bin/python3
"""The module presents functions to manipulate matrices
1) matrix_divided
    Args: matrix, div
    Return: new manipulated matrix
"""


def matrix_divided(matrix, div):
    """Function divides all elements of matrix by div
    Args:
        matrix (list of lists) of integer or float elements
        div (float or integer)
    Return:
        new matrix
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix " +
                        "(list of lists) of integers/floats")
    length = len(matrix) - 1
    row_length = len(matrix[length])
    result = []
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix " +
                            "(list of lists) of integers/floats")
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        inner = []
        for dat in row:
            if type(dat) not in [int, float]:
                raise TypeError("matrix must be a matrix " +
                                "(list of lists) of integers/floats")
            inner.append(round(dat / div, 2))
        result.append(inner)
    return result
