#!/usr/bin/python3

say_my = __import__('3-say_my_name').say_my_name

say_my("John", "Smith")
say_my("Walter", "White")
say_my("Bob")

try:
    say_my(12, "White")
except Exception as e:
    print(e)
