#!/usr/bin/python3
"""returnin gdict of class"""


def class_to_json(obj):
    """need to get dict of obj

    Args:
        obj: can be anything
    """
    return obj.__dict__
