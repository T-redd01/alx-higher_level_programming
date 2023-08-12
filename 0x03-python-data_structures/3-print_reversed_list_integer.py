#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """print list of integers in reverse

        Args:
            my_list: list of integers
    """
    x = my_list[:]
    for i in x.reverse():
        print("{:d}".format(my_list[i]))
