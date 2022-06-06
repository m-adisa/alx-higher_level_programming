#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    lips = []
    for i in my_list:
        if i % 2 == 0:
            lips.append(True)
        else:
            lips.append(False)

    return lips
