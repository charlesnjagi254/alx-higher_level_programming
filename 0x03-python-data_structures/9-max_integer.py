#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return

    large = my_list[0]
    for i i range(1, len(my_list)):
        if large < my_list[1]:
            large = my_list[i]
        else:
            continue
        return large

