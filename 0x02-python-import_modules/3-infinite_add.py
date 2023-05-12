#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number_of_arguments = len(argv) - 1
    if number_of_arguments == 0:
        print("{}".format(0))
    else:
        a = int(argv[1])
        b = int(argv[2])
        print("{}".format(a + b))
