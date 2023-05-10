#!/usr/bin/python3
alpha = ""
for i in range(26):
    if i not in (4, 16):
        alpha = alpha + chr(ord("a") + i)
print("{}".format(alpha), end="")
