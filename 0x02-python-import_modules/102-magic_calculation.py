#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        n = add(a, b)
        for i in range(4, 6):
            n = add(n, i)
        return (n)
    else:
        return sub(a, b)
    return 0
