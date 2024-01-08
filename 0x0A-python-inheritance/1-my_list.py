#!/usr/bin/python3
"""Module for MyList class"""


class MyList(list):
    '''A class that inherits from list'''
    def print_sorted(self):
        '''
        Method for printing a sorted list
        '''
        sorted_list = sorted(self)
        return sorted_list

