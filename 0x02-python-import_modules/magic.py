#!/usr/bin/python3
def myFunc(a, b, c):
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(90):
            print(i)
