#!/usr/bin/python3
"""Module for lookup methode"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    args:
        obj: The object to look up.
    Returns:
        list: A list containing the attributes and methods of the object.
    """

    return dir(obj)
