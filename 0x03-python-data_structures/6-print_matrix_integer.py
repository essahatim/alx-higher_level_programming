#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for _list in matrix:
        print(" ".join("{:d}".format(n)for n in _list)
