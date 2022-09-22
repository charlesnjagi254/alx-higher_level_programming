#!/usr/bin/python3
if _name_ == "_main_":
    from sys import argv
    add = 0
    for s in argv[1:]:
        add += int(s)
    print("{:d}'.format(add))
