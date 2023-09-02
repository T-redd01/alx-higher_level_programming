#!/usr/bin/python3
"""contains function matrix divide"""


def matrix_divided(matrix, div):
    """divides elements of matrix by div

    Args:
        matrix (list): a list of lists
        div (int): value to divide each element by

    Returns:
        new matrix with divided elements
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    try:
        if isinstance(matrix[0], list):
            row_len = len(matrix[0])
    except Exception:
        pass

    new = []
    for i in matrix:
        if not isinstance(i, list) or i == []:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        if len(i) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        app = []
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
            app.append(round(j / div, 2))
        new.append(app)
    return new
