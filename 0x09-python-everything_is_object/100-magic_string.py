#!/usr/bin/python3
def magic_string():
    magicStr.count = getattr(magicStr, 'count', 0) + 1
    return ', '.join(['BestSchool' for _ in range(magicStr.count)])
