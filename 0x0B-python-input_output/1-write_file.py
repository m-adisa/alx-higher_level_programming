#!/usr/bin/python3
"""Module 1-write_file.py
1) write_file
"""


def write_file(filename="", text=""):
    """Function that writes to a file
    Args:
        - filename
        - text
    Return:
        The number of characters written
    """
    with open(filename, 'w', encoding="UTF-8") as f:
        return f.write(text)
