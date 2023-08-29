#!/usr/bin/python3
"""My first class part 3"""


class Square:
    """class Square, about a square

    Attributes:
        __size (int): size of square
    """

    def __init__(self, size=0):
        """Initialize square

        Args:
            size (int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """finds area of the square

        Returns:
            size to the power of 2
        """
        return self.__size ** 2
