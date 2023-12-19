#!/usr/bin/python3

class Square:

    def __init__(self, size=0):
        self.size = size

    # getter to retrieve the size
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        '''
        heck if the provided size is an integer
        Check if the provided size is greater than or equal to 0
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    # calculate and return the square area
    def area(self):
        return self.__size ** 2
