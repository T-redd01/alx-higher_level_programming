#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    mul_tups = sum((i * j for i, j in my_list))
    add_2_el = sum((j for i, j in my_list))
    return mul_tups / add_2_el
