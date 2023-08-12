#!/usr/bin/python3
def element_at(my_list, idx):
    """retrieves value of given index in list

        Args:
            my_list: list of values
            idx: index of wanted value

        Returns:
            value from my_list at idx or none
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
