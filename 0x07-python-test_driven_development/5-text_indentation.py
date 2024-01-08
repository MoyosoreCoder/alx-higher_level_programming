#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c_count = 0
    while c_count < len(text) and text[c_count] == ' ':
        c_count += 1

    while c_count < len(text):
        print(text[c_count], end="")
        if text[c_count] == "\n" or text[c_count] in ".?:":
            if text[c_count] in ".?:":
                print("\n")
            c_count += 1
            while c_count < len(text) and text[c_count] == ' ':
                c_count += 1
            continue
        c_count += 1
