#!/usr/bin/python3
"""Module 6-load_from_json_file.py
1) load_from_json_file(filename)
"""


def load_from_json_file(filename):
    """Creates an object from a JSON file
    Args:
        - filename
    Return:
        - Python object
    """
    import json
    with open(filename, encoding="UTF-8") as f:
        return json.load(f)
