#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    data = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    count = 0
    prev = 0
    rom_l = roman_string.upper()

    for i in rom_l:
        if i in data:
            count += data[i]
            if data[i] > prev:
                count -= prev * 2
            prev = data[i]
        else:
            return 0
    return count
