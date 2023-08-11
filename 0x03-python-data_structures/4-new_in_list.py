#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """create copy of list with different value at index

        Args:
            my_list: list to copy
            idx: index for new val
            elemnt: new val for idx

        Return:
            copy of list with elemnet at idx
    """
    return [element if i == idx else v for i, v in enumerate(my_list)]
