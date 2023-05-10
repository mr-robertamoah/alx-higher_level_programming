#!/usr/bin/python3
for i in range(26):
    alpha = chr(ord("a") + i)
    if alpha not in "qe":
        print("{}".format(alpha), end="")
