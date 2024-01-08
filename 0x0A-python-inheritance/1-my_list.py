#!/usr/bin/python3
"""Module for MyList class"""


class MyList(list):
    '''A class that inherits list'''
    def print_sorted(self):
        '''
        Method for printing a sorted list
        '''
        sorted_list = sorted(self)
        print(sorted_list)
