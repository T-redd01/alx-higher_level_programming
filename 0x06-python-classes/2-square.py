#!/usr/bin/python3
"""My first class part 3"""


class Square:
    """class Square, checking attribute in init

    Attributes:
        __size (int): size of square
    """

    def __init__(self, size=0):
        """Initializes instance of square

        Args:
            size (int): optional parameter for square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
