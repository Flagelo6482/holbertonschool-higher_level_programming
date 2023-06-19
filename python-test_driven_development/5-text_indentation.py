#!/usr/bin/python3
"""
Text indentation
"""


def text_indentation(text):
    """Function that prints a text"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0

    while i < len(text):
        if text[i] in [".", "?", ":"]:
            print(f"{text[i]}\n")
            i += 2
        else:
            print(text[i], end="")
            i += 1
