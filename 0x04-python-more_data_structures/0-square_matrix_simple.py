#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if isinstance(matrix, list) and len(matrix):
        return [[x**2 for x in row] for row in matrix]
