#!/usr/bin/python3
'''Square module'''


class Square:
    '''Defines square'''

    def __init__(self, size=0):
        self.size = size

    '''Getter to retrieve the size'''
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Check if the provided size is an integer
        Check if the provided size is greater than or equal to 0
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    '''Calculate and return the square area'''
    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            '''Print an empty line if size is 0'''
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
