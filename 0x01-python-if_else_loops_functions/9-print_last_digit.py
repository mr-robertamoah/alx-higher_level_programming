#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    last_d = number % 10
    print(f"{last_d}", end="")
    return last_d
