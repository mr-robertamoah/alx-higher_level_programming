#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number_of_arguments = len(argv) - 1
    if number_of_arguments == 0:
        print("{}".format(0))
    else:
        i = 0
        result = 0
        for a in argv:
            if i != 0:
                result += int(a)
            i += 1
        print("{}".format(result))
