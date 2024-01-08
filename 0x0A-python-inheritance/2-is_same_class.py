#!/usr/bin/python3
"""Module for the is_same_class method"""


def is_same_class(obj, a_class):
    '''Chek if the object is exactly an instance of the specified class'''
    return type(obj) is a_class
