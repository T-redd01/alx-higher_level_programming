#!/usr/bin/python3
"""subclasses checking"""


def inherits_from(obj, a_class):
    """check if obj inherits from

    Args:
        obj: obj to check
        a_class: class to check against

    Return:
        True if inherited else false
    """
    if issubclass(a_class, type(obj)):
        return True
    return False
