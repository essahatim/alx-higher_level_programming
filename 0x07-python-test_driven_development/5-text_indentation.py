#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text: The input text.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        # Print the character without leading or trailing spaces
        print(char, end="")
        if char in ['.', '?', ':']:
            print("\n\n", end="")

    # Print a newline at the end if necessary
    if text and text[-1] not in ['.', '?', ':']:
        print()

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
