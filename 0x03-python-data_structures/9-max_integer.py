#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        new_list = sorted(my_list)
        return new_list[-1]
