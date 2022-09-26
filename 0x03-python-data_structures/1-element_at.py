#!/usr/bin/python3

# retrives an element from a list as in C.

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return
    return my_list[idx]
