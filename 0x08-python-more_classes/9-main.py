#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
new_square = eval(repr(my_square))
print(my_square)
print("--")
print(new_square)
try:
    mysquare = Rectangle.square(-2)
    print("{} / {}".format(mysquare.width, mysquare.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
