#!/usr/bin/python3
def complex_delete(a_dict, value):
    a_dict = {key: v for key, v in a_dict.items() if v != value}
