#!/usr/bin/python3
"""Module 3-to_json_string
1) to_json_string
"""


def to_json_string(my_obj):
    """Function to return the json representation of my_obj
    Args:
        - my_obj
    Return:
        JSON representation"""
    import json
    return json.dumps(my_obj)
