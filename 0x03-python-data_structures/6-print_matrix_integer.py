#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    matrix_len = len(matrix)
    if matrix_len == 0 or (matrix_len == 1 and len(matrix[0]) == 0):
        print()

    if isinstance(matrix, list):
        for i in range(matrix_len):
            if isinstance(matrix[i], list):
                for j in range(len(matrix[i])):
                    if j + 1 == len(matrix[i]):
                        print("{:d}".format(matrix[i][j]))
                    else:
                        print("{:d} ".format(matrix[i][j]), end="")
