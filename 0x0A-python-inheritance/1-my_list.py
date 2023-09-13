#!/usr/bin/python3
"""inheriting from list"""


class MyList(list):
    """Practice inheriting"""
    def print_sorted(self):
        """print list sorted"""
        my_l = self.copy()
        my_l.sort()
        print(my_l)
