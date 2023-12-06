#!/usr/bin/python3
def roman_to_int(roman_string: str):

    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    numbers = [roman_num[char] for char in roman_string] + [0]
    total = 0
    for current, next_num in zip(numbers, numbers[1:]):
        total += current if current >= next_num else -current
    return total
