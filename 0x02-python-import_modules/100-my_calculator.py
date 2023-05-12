#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    number_of_arguments = len(argv) - 1
    if number_of_arguments < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    result = 0;
    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "*":
        result = mul(a, b)
    elif op == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, op, b, result))
