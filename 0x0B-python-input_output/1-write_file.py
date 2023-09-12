#!/usr/bin/python3
"""writing to a file"""


def write_file(filename="", text=""):
    """writing to a file

    Args:
        fielname: name of file
        text (str): string to write
    """
    with open(filename, "w") as f:
        num = f.write(text)
        return num
