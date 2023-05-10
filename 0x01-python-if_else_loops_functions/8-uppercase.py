#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ascii_v = ord(c)
        char = c
        if ascii_v >= 97 and ascii_v <= 122:
            char = chr(ascii_v - 32)
        print("{}".format(char), end="")
    print("")
