#!/usr/bin/python3
def no_c(my_string):
    """removes c and C from string

        Args:
            my_string: string sequence

        Return:
            new string without c and C characters
    """
    return "".join(i for i in my_string if i not in "cC")
