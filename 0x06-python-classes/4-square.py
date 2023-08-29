#!/usr/bin/python3
"""My first class part 4"""


class Square:
    """class Square, about a square

    Attributes:
        __size (int): size of a square
    """

    def __init__(self, size=0):
        """Initializes a square instance

        Args:
            size (int): size of square
        """
        self.size = size

    @property
    def size(self):
        """This is a getter method for size

        the setter method checks if arg is less than 0
        and also if it is an int
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """get area of square

        Returns:
            area of square (size to the power of 2)
        """
        return self.__size ** 2
