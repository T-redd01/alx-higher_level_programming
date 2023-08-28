#!/usr/bin/python3
from sys import stderr

def safe_function(fct, *args):
    res = None
    try:
        res = fct(*args)
    except Exception as err:
        print("Exception: ", err, file=stderr)
    return res
