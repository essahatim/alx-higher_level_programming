#!/usr/bin/python3
'''Difine  pascal_triangle function'''


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    Pascal's triangle of n
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
