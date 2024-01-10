#!/usr/bin/python3
'''Module of class_to_json function'''


def class_to_json(obj):
    """
    Return the dictionary description with a simple data
    structure for JSON serialization of an object
    """
    return obj.__dict__
