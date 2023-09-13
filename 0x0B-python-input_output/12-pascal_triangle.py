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

    new = [[1]]
    foo = new[0]
    tmp = []

    for i in range(n - 1):
        tmp = []
        for j in range(len(foo)):
            if j == 0:
                tmp.append(foo[j])

            if j + 1 != len(foo):
                tmp.append(foo[j] + foo[j + 1])
            else:
                tmp.append(foo[j])
        new.append(tmp)
        foo = tmp
    return new
