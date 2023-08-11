#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """delete element of a list

        Args:
            my_list: list to delete element from
            idx: index to delete from list

        Return:
            list with removed element
    """
    if idx < 0 or idx >= len(my_list):
        pass
    else:
        del my_list[idx]
    return my_list
