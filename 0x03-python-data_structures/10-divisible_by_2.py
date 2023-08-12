#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """checks if each elemetn in list is multiple of 2

        Args:
            my_list: list of integers

        Return:
            new list with true for element that is multiple of 2
    """
    return [True if i % 2 == 0 else False for i in my_list]
