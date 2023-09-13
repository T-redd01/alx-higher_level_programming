#!/usr/bin/python3
"""can i add attr or not"""


def add_attribute(obj, name, value):
    """sets an attribute

    Args:
        obj: class to set attr
        name: name of new attr
        value: value of attr
    """
    try:
        setattr(obj, name, value)
    except AttributeError:
        raise TypeError("can't add new attribute")
