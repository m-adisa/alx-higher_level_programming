#!/usr/bin/python3
"""Module 100-append_after
1) append_after(filename, search_string, new_string
"""


def append_after(filename="", search_string="", new_string=""):
    """A function that inserts a line of text into a file
    after each line containing a specific string
    Args:
        - filename
        - search_string
        - new_string
    """
    st = ""
    with open(filename, 'r', encoding="UTF-8") as f:
        for line in f:
            st += line
            if search_string in line:
                st += new_string

    with open(filename, 'w', encoding="UTF-8") as fo:
        fo.write(st)
