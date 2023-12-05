#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    if not matrix:
        return
    else:
        for my_list in range(len(matrix)):
            for i in range(len(matrix[my_list])):
                if i != len(matrix[my_list]) - 1:
                    space = " "
                else:
                    space = ""
                print("{:d}".format(matrix[my_list][i]), end=space)
            print()
