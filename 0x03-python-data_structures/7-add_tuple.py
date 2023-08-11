#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """adds 1st and 2nd value in tuples

        Args:
            tuple_a: 1st tuple to add
            tuple_b: 2nd tuple to add

        Return:
            new tuple with 1st and 2nd tuples 0 idx added and 1 idx added
    """
    x = [0, 0]
    for i, v in enumerate(tuple_a):
        if i == 2:
            break
        x[i] += v

    for i, v in enumerate(tuple_b):
        if i == 2:
            break
        x[i] += v

    return tuple(x)
