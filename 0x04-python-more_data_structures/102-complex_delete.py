#!/usr/bin/python3
def complex_delete(a_dictionary, value):

    my_list = {key: v for key, v in a_dictionary.items() if v != value}
    a_dictionary = my_list
