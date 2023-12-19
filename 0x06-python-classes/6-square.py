#!/usr/bin/python3
'''Square module'''


class Square:
    '''Defines square'''

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    '''Getter to retrieve the size'''
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

    '''Getter to retrieve the position'''
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        '''Check if the provided position is a tuple of 2 positive integers'''
        if not (isinstance(value, tuple) and
                len(value) == 2 and
                all(isinstance(coord, int) and coord >= 0 for coord in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    '''Calculate and return the square area'''
    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            '''Print an empty line if size is 0'''
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
