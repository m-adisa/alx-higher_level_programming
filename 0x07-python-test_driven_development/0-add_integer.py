#!/usr/bin/python3
"""Module contains a function for manipulating integers
1) add_integer
    Args: a, b
    Return: a + b
"""


def add_integer(a, b=98):
    """Function to add integers
    Args: a, b (default to 98)
        Arguments have to be integers or floats
    Return: the integer addition of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
