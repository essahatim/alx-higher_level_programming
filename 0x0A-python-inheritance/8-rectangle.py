#!/usr/bin/python3
"""Module for an Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass  rectangle """

    def __init__(self, width, height):
        '''Initializes a Rectangle object with width and height'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
