#!/usr/bin/python3
"""Module 4-from_json_string
1) from_json_string(my_str)
"""


def from_json_string(my_str):
    """Function to return a python data structure
    from a JSON string
    Args:
        - my_str
    Return:
        - Python data sructure
    """
    import json
    return json.loads(my_str)
