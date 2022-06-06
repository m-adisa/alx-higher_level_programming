#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        stu = 0, None
    else:
        stu = len(sentence), sentence[0]
    return stu
