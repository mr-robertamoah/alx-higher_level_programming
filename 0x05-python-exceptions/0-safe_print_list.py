#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    no_of_items = 0
    try:
        for v in my_list:
            if no_of_items == x:
                print()
                return no_of_items

            print("{}".format(v), end="")
            no_of_items += 1
    except Exception:
        print()
        return no_of_items
    print()
    return no_of_items
