#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    length = int(length)
    if length == 1:
        print(f"{(length - 1):d} arguments.")
    elif length == 2:
        print(f"{(length - 1):d} argument:")
    elif length > 2:
        print(f"{(length - 1):d} arguments:")

    for i in range(1, length):
        print(f"{i}: {argv[i]}")
