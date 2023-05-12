#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number_of_arguments = len(argv) - 1
    if number_of_arguments == 1:
        a = ""
    else:
        a = "s"
    if number_of_arguments == 0:
        b = "."
    else:
        b = ":"
    print("{} argument{}{}".format(number_of_arguments, a, b))
    if number_of_arguments != 0:
        for i in range(1, number_of_arguments + 1):
            print("{}: {}".format(i, argv[i]))
