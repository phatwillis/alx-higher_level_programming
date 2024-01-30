#!/usr/bin/python3

def add_integer(a, b=98):
    """
    a function that adds integers and returns the result
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        if type(a) == float:
            a = int(a)
        if type(b) == float:
            b = int(b)
        return a + b
