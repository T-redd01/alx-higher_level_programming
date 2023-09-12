#!/usr/bin/python3
"""loading json strings"""
import json


def from_json_string(my_str):
    """turning it into an obj

    Args:
        my_str (str): strign repr

    Return:
        obj of repr
    """
    obj = json.loads(my_str)
    return obj
