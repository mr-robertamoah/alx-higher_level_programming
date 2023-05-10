#!/usr/bin/python3
def islower(c):
    ascii_v = ord(c)
    if ascii_v >= 97 and ascii_v <= 122:
        return True
    return False
