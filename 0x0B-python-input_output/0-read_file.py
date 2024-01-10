#!/usr/bin/python3
'''Module of read_file function'''


def read_file(filename=""):
    """Read the contents of a text file and print it to stdout"""
    with open(filename, encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
