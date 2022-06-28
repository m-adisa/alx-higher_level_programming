#!/usr/bin/python3
def magic_string(i=[0]):
    i[0] += 1
    return str("Best School, " * (i[0] - 1)) + "Best School"
