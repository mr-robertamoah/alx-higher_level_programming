#!/usr/bin/python4

"""
Contains matrix_divided function that divides the elements of a function
by a number

"""


def matrix_divided(matrix, div):
    """
    Divides all elements of matrix

    Args:
        matrix ([[]]): list of lists of int and float
        div (int or float): a non zero number

    Returns:
        [[]]: a list of lists containing divisions made on elements
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise TypeError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    m_element_len = 0
    if len(matrix) and isinstance(matrix[0], list):
        m_element_len = len(matrix[0])

    new_matrix = []
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

        if m_element_len != len(i):
            raise TypeError("Each row of the matrix must have the same size")

        inner_matrix = []
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            inner_matrix.append(round(j / div, 2))
        new_matrix.append(inner_matrix)

    return new_matrix
