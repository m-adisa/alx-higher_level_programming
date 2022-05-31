#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp_num = number

if number < 0:
    number = -number


if (number % 10) > 5:
    print(f"Last digit of {temp_num:d} is {(number % 10):d} and is greater than 5")
elif (number % 10) == 0:
    print(f"Last digit of {temp_num:d} is {(number % 10):d} and is 0")
elif (number % 10) < 6 and (number % 10) != 0:
    print(f"Last digit of {temp_num:d} is {(number % 10):d} and is less than 6 and not 0")
