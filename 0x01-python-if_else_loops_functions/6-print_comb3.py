#!/usr/bin/python3
for i in range(9):
    j = i + 1
    while j < 10:
        print("{}{}, ".format(i, j), end="")
        j += 1
print("")
