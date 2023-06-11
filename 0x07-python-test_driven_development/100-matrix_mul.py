#!/usr/bin/python3

"""
Contains a matrix_mul function that multiplies
two list of lists containing ints and floats

"""


def matrix_mul(m_a, m_b):
    """
    Multiply two list of lists containing integers and floats

    Args:
        m_a (list of lists): list of lists containing ints and floats
        m_b (list of lists): list of lists containing ints and floats
    Returns:
        list of lists containing ints and floats
    """
    number_of_rows_m_b = 0
    number_of_columns = 0
    matrix = []

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")

    column_track = len(m_a[0])
    for m in m_a:
        if not isinstance(m, list):
            raise TypeError("m_a must be a list of lists")

        number_of_columns = len(m)

        if number_of_columns == 0:
            raise ValueError("m_a can't be empty")

        for i in m:
            if not isinstance(i, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

        if column_track != number_of_columns:
            raise TypeError("each row of m_a must be of the same size")
    number_of_columns_m_a = number_of_columns

    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    column_track = len(m_b[0])
    for n in m_b:
        if not isinstance(n, list):
            raise TypeError("m_b must be a list of lists")

        number_of_rows_m_b += 1
        number_of_columns = len(n)

        if number_of_columns == 0:
            raise ValueError("m_b can't be empty")

        for j in n:
            if not isinstance(j, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

        if column_track != number_of_columns:
            raise TypeError("each row of m_b must be of the same size")

    if number_of_rows_m_b != number_of_columns_m_a:
        raise ValueError("m_a and m_b can't be multiplied")

    new_row = []
    for m_a_r in m_a:
        for i in range(number_of_columns):
            column_as_row = []
            for m_b_r in m_b:
                column_as_row.append(m_b_r[i])
            summed = 0
            for i in range(len(m_a_r)):
                summed += (m_a_r[i] * column_as_row[i])
            new_row.append(summed)
        matrix.append(new_row)
        new_row = []

    return matrix
