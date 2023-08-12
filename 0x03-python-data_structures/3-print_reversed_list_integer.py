#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """print list of integers in reverse

        Args:
            my_list: list of integers
    """
    x = my_list.copy()
    x.reverse()
    for i in x:
        print("{:d}".format(i))
"""

my_list = [1,2,3,4,5,6]
print_reversed_list_integer(my_list)
print()

my_list = []
print_reversed_list_integer(my_list)
print()

my_list = None
print_reversed_list_integer(my_list)
print()

my_list = [1, 2, "str", 4, 5]
print_reversed_list_integer(my_list)
"""
