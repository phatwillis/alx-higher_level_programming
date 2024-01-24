#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
        return x
    except IndexError:
        print()
        for i in my_list:
            counter += 1
        return counter
