#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    loop = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return loop
    else:
        loop[idx] = element
        return loop
