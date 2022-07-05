#!/usr/bin/python3
"""Module reads the text from a file
1) read_file: reads file text
"""


def read_file(filename=""):
    """Function reads text from a file
    Args:
        filename
    Return:
        Prints to stdout
    """
    with open(filename, encoding="UTF-8") as a_file:
        read_t = a_file.read()
        print(read_t, end="")
