#!/usr/bin/python3
"""Module for add_integer method"""


def add_integer(a, b=98):
    '''
    adds 2 integers.
    args:
        a : First integer or float.
        b : Second integer or float by default 98.
    Raises:
        TypeError: If a or b not an integer or a float.
    Return:
        The sum of a and b.
    '''

    if a not in (int, float):
        raise TypeError("a must be an integer")
    if b not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
