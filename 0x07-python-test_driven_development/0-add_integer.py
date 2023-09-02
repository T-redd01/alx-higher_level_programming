#!/usr/bin/python3
"""practice test driven development on addition function"""


def add_integer(a, b=98):
    """add 2 nummbers

    Args:
        a (int): first number
        b (int): second number

    Returns:
        addition of both integers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
