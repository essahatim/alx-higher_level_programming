#!/usr/bin/python3
'''Function append_write with args'''


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8)
    and return the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
