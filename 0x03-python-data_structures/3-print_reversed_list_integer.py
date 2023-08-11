#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """print list of integers in reverse

        Args:
            my_list: list of integers
    """
    for i in range((len(my_list) - 1), -1, -1):
        print("{:d}".format(my_list[i]))
