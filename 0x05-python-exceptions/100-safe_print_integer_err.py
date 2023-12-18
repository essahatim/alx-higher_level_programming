#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    an_integer = True
    try:
        print("{:d}".format(value))
    except Exception as e:
        print('Exception:', e, file=sys.stderr)
        an_integer = False
    return an_integervalue
