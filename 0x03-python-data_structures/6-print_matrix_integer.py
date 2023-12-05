#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    if not matrix:
        return None
    else:
        for my_list in matrix:
            for i in matrix[my_list]:
                if i != matrix[my_mylist] - 1:
                    space = " "
                else:
                    space = ""
                print(" " + "{:d}".format(matrix[my_list][i]), end=space)
            print()
