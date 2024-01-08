#!/usr/bin/python3
"""Module for an Rectangle class"""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """A claas child """

    def __init__(self, width, height):
        '''Initializes a Rectangle object with width and height'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Computes and returns the area of the rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''A string representation of the rectangle'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
