#!/usr/bin/python3
"""Module 2-append_write.py
1) append_write
"""


def append_write(filename="", text=""):
    """Function to addend to a file
    Args:
        - filename
        - text
    Return:
        The number of files written
    """
    with open(filename, 'a', encoding="UTF-8") as f:
        return f.write(text)
