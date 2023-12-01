#!/usr/bin/python3
""" a peak in a list is a number >= its neighbour """


def find_peak(list_of_integers):
    """ find first peak in list """
    if len(list_of_integers) == 0 or not isinstance(list_of_integers, list):
        return None

    beg = 0
    end = len(list_of_integers) - 1
    i = 0
    my_l = list_of_integers
    while i <= len(my_l):
        mid = (beg + end) // 2
        if my_l[mid] > my_l[mid + 1] and my_l[mid] > my_l[mid - 1]:
            return my_l[mid]
        if my_l[mid + 1] > my_l[mid - 1]:
            beg = mid + 1
        else:
            end = mid - 1
        i += 1
    return my_l[mid]
