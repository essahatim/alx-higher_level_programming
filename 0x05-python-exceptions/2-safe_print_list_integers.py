#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0
    value = my_list[i]
    while i < x:
        try:
            print('{:d}'.format(value), end='')
            count += 1
        except (ValueError, TypeError):
            pass
        i += 1
    print()
    return count
