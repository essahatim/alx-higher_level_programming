#!/usr/bin/python3
"""Module for an class BaseGeometry"""


class BaseGeometry:
    def area(self):
        '''Raises an Exception with an message'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validates the value'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
