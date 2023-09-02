#!/usr/bin/python3
"""file for function that prints square with # character"""


def print_square(size):
    """prints a square using # and size

    Args:
        size (int): length of the square
    """
    if (isinstance(size, float) and size < 0) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("")

    for i in range(size):
        print(f"{'#' * size}")
