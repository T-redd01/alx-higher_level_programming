#!/usr/bin/python3
"""check the instance"""


def is_kind_of_class(obj, a_class):
    """checking instance"""
    if isinstance(obj, a_class):
        return True
    return False
