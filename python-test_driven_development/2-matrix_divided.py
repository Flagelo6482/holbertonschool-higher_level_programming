#!/usr/bin/python3
"""
Divide

a Matrix
"""


def matrix_divided(matrix, div):
    """
    Function to divide the elements of a list
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    for i in matrix:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(message)

    m_len = len(matrix[0])
    for i in matrix[1:]:
        if len(i) != m_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")

    new_list = matrix.copy()
    for i in range(len(matrix)):
        new_list[i] = list(map(lambda x: round(x / div, 2), matrix[i]))
    return new_list
