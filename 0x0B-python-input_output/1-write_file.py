#!/usr/bin/python3
'''Function write_file with args'''


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8)
    and return the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
