#!/usr/bin/python3
'''
Defines an class Rectangle
'''


class Rectangle:
    '''Representation of a rectangle'''
    def __init__(self, width=0, height=0):
        '''Initialize the Rectangle instance with optional width and height'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Getter method for retrieving the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter method for setting the width of the rectangle'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''Getter method for retrieving the height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter method for setting the height of the rectangle'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''Calculate and return the area of the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Calculate and return the perimeter of the rectangle'''
        if self.__width != 0 and self.__height != 0:
            return 2 * (self.__width + self.__height)
        else:
            return 0

    def __str__(self):
        '''Return a string representation of the rectangle'''
        rectangle_str = ""
        if self.__width != 0 and self.__height != 0:
            row_str = "#" * self.__width
            rectangle_str += "\n".join(row_str for i in range(self.__height))
        return rectangle_str
