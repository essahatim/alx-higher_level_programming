#!/usr/bin/python3
"""Module for the is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    '''Chek if the object is an instance of, or of a class that inherited'''
    return isinstance(obj, a_class)
