#!/usr/bin/python3
"""Module for an Square class"""
Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    """A class dirvied"""

    def def __init__(self, size):
        '''Initializes a Square object with a given size'''
        self.integer_validator("size", size)
        self.size = size
        super().__init__(size, size)

    def area(self):
        '''The area method of square'''
        return self.__size ** 2

    def __str__(self):
        ''' A  string representation of the square'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
