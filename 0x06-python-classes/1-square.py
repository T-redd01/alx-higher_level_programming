#!/usr/bin/python3
"""My first class part 2"""


class Square:
    """class Square, private instance attribute size

    Attributes:
        __size (int): private attribute
    """

    def __init__(self, size):
        """Initializer method

        Args:
            size (int): size of square
        """
        self.__size = size
