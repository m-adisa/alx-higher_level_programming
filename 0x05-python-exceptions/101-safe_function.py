#!/usr/bin/python3

def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
        return result
    except Exception as ne:
        print("Exception: {}".format(ne), file=sys.stderr)
        return None


def my_div(a, b):
    return a / b
