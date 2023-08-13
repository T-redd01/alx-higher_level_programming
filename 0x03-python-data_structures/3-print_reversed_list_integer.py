#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """print list of integers in reverse

        Args:
            my_list: list of integers
    """
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
