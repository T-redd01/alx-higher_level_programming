#!/usr/bin/python3
"""appending lines"""


def append_after(filename="", search_string="", new_string=""):
    """appends to file

    Args:
        filename: name of file
        search_string: string to search for
        new_string: string to replace
    """
    counter = 0
    new = ""
    with open(filename, "r") as f:
        for line in f:
            new += line
            if search_string in line:
                new += new_string
    with open(filename, "w") as f:
        f.write(new)
