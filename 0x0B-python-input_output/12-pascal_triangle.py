#!/usr/bin/python3
"""what is pascals triangle"""


def pascal_triangle(n):
    """make list of lists for pascals tri

    Args:
        n (int): stop point

    Returns:
        list of lists with triangle
    """
    if n <= 0:
        return []
