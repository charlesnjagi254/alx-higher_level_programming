#!/bin/usr/python3

def common_elements(set_1 & set_2):
    result = False
    for x in set_1:
        for y in set_2:
            if x ==y:
                result = True
                return result
