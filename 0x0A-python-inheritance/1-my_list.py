#!/usr/bin/python3
"""inheriting from list"""


class MyList(list):
    """Practice inheriting"""
    def print_sorted(self):
        """print list sorted"""
        my_l = self.copy()
        my_l.sort()
        print("[", end='')
        for i in range(len(my_l)):
            if i == 0:
                print(f"{my_l[i]:d}", end='')
                continue
            print(f", {my_l[i]:d}", end='')
        print("]")
