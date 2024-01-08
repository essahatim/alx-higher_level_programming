#!/usr/bin/python3
"""Module the class MyInt"""


class MyInt(int):
    """A class MyInt"""

    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """Inverts the behavior of the == operator"""
        return int(self) != other

    def __ne__(self, other):
        """Inverts the behavior of the != operator"""
        return int(self) == other
