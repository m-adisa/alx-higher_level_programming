#!/usr/bin/python3
"""Module 8-class_to_json
1) class_to_json(obj)
"""


def class_to_json(obj):
    """Returns the dict description with a simple data structure
    for JSON serialization of an object
    Args:
        - obj
    """
    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
