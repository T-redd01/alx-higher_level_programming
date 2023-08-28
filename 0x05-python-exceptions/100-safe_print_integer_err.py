#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    ret = True
    try:
        print("{:d}".format(value))
    except Exception as err:
        print("Exception: {}".format(err), file=stderr)
        ret = False
    return ret
