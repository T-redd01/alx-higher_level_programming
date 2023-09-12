#!/usr/bin/python3
"""appending to file"""


def append_write(filename="", text=""):
    """adds to file

    Args:
        filename: name of file
        text (str): to add

    Returns:
        number of chars added
    """
    with open(filename, "a") as f:
        num = f.write(text)
        return num
