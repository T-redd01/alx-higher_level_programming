#!/usr/bin/python3
def remove_char_at(str, n):
    """remove charater from string

        Args:
            str: tring to copy
            n: index to skip

        Return:
            new string without character at index
    """
    new = ""
    for i, v in enumerate(str):
        if i == n:
            continue
        new += v

    return new


print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
