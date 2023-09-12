#!/usr/bin/python3
"""read from file"""


def read_file(filename=""):
    """reads from file

    Args:
        filename: a file
    """
    with open(filename, "r") as f:
        r = f.read()
        print(r)
