#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """print list of integers in reverse

        Args:
            my_list: list of integers
    """
    x = my_list[:]
    x.reverse()
    for i in x:
        print("{:d}".format(i))
