#!/usr/bin/python3
"""creating function say my name"""


def say_my_name(first_name, last_name=""):
    """formats args into string

    Args:
        first_name (str): first name of person
        last_name (str): last name / surname of person
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name:s} {last_name:s}")
