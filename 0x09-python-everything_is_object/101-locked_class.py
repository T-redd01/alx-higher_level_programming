#!/usr/bin/python3
"""create locled class"""


class LockedClass:
    """class without dynamic attrib creation"""
    __slots__ = ["first_name"]
