#!/usr/bin/python3
"""first json func"""
import json


def to_json_string(my_obj):
    """create json repr

    Return:
        json repr
    """
    string = json.dumps(my_obj)
    return string
