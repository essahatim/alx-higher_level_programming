#!/usr/bin/python3
'''
Defines a locke class
'''


class LockedClass:
    '''
    Prevent the user from instantiating the attribute being set is first_name
    '''

    __slots__ = ["first_name"]
