#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    new_list = []
    for i in my_list:
        num = (i % 2 == 0)
        new_list.append(num)
    return new_list
