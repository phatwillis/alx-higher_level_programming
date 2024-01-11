#!/usr/bin/python3

def uniq_add(my_list=[]):
    set_list = set(my_list)
    new_list = []
    summed = 0
    for i in set_list:
        new_list.append(i)
    for i in range(len(new_list)):
        summed += new_list[i]
    return summed
