#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """replace value at given index of list
    
        Args:
            my_list: list to change value
            idx: index of list value to change
            element: new value of list at index

        Return:
            returns original list with either new value at idx or unchanged
    """
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return my_list
