#!/usr/bin/python3
"""My first class part 6"""


class Square:
    """class Square, about a square

    Attributes:
        __size (int): size of square
        __position (tuple): tuple with int coordinates
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes instance of square

        Args:
            size (int): size of square
            position (tuple): tuple of int coordinates of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter method to retrieve size

        setter method will check type and value for size
        before assignment and raise errors accordingly
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """getter method for position of square

        setter method validates whether or not value is a tuple
        of 2 ints and raises errors accordingly
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
                or not isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """get area of square

        Returns:
            __size raised by 2
        """
        return self.__size ** 2

    def my_print(self):
        """print the square using # char"""

        print("{}".format('\n' * self.__position[1]), end='')
        for i in range(self.__size):
            print("{}".format(' ' * self.__position[0]), end='')
            for j in range(self.__size):
                print("#", end='')
            print("")
