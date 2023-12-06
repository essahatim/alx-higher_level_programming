#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    sub_matrix = [[e ** 2 for e in line] for line in matrix]
    return sub_matrix
