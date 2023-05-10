#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new_n = number
if number < 0:
    new_n = new_n * -1
last_d = new_n % 10
if number < 0:
    last_d = last_d * -1
if last_d > 5:
    str = "and is greater than 5"
elif last_d == 0:
    str = "and is 0"
else:
    str = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last_d} {str}")
