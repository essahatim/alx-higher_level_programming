#!/usr/bin/python3
"""Module for the inherits_from method"""


def inherits_from(obj, a_class):
    '''Chek if the object is an instance of a class that inherited'''
    return isinstance(obj, a_class) and type(obj) != a_class
