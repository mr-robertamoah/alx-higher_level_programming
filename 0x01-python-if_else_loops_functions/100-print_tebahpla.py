#!/usr/bin/python3
for i in range(26):
    if i % 2 == 0:
        letter = chr(ord("z") - i)
    else:
        letter = chr(ord("z") - i - 32)
    print("{}".format(letter), end="")
