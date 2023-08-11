#!/usr/bin/python3
def max_integer(my_list=[]):
    """finds max integer in list

        Args:
            my_list: list to look through

        Return:
            largest number in list
    """
    if my_list == []:
        return None

    largest = my_list[0]
    for i in my_list:
        if i > largest:
            largest = i
    return largest
