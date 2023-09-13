#!/usr/bin/python3
"""class to inheret from int"""


class MyInt(int):
    """class inheret from int"""

    def __eq__(self, other):
        """return equality in opposite"""
        if super().__eq__(other):
            return False
        return True

    def __ne__(self, other):
        """return equality in opposite"""
        if super().__ne__(other):
            return False
        return True
