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
    if isinstance(type(obj), a_class):
        return False
    if issubclass(type(obj), a_class):
        return True
    return False
