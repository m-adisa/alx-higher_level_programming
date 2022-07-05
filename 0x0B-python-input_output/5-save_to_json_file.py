#!/usr/bin/python3
"""Module 5-save_to_json_file
1) save_to_json_file
"""


def save_to_json_file(my_obj, filename):
    """Function to write an object to a text file using JSON representation
    Args:
        - my_obj
        - filename
    """
    import json
    with open(filename, 'w+', encoding="UTF-8") as f:
        json.dump(my_obj, f)
