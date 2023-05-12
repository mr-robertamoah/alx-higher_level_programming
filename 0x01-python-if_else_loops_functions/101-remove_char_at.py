#!/usr/bin/python3
def remove_char_at(str, n):
    i = -1
    for c in str:
        i += 1
        if i != n:
            print(c, end="")
    return ""
