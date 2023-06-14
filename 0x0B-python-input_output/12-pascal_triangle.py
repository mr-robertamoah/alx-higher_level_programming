#!/usr/bin/python3

"""
Contains pascal_triangle function
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s
    triangle of n

    Args:
        n (int): integer used to build the pascal triangle
    """

    matrix = []
    for i in range(1, n + 1):
        row = prev_row = []
        if i > 1:
            prev_row = matrix[i - 2]
        for j in range(i):
            if j == 0 or j + 1 == i:
                row.append(1)
            # elif (n / 2) >= (float) j:
                # row.append(prev_row[j] + prev_row[j - 1])
            else:
                row.append(prev_row[j] + prev_row[j - 1])
        matrix.append(row)
    return matrix
