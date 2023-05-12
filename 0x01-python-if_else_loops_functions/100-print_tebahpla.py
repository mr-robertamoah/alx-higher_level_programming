#!/usr/bin/python3
for i in range(25):
    if i % 2 == 0:
        letter = chr(ord("y") - i)
    else:
        letter = chr(ord("y") - i - 32)
    print(f"{letter}", end="")
