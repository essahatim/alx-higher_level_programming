#!/usr/bin/python3
'''Difine to_json_string function'''


import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string)"""
    return json.dumps(my_obj)
