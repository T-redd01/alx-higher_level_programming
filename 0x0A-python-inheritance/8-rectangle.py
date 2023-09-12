#!/usr/bin/python3
"""empty class here"""


class BaseGeometry:
    """an empty class"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if value is int

        Args:
            name (str): name to print
            value (int): should be an int

        Return:
            true if is int else raise exception
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return True


class Rectangle(BaseGeometry):
    """class about rectangle

    Attributes:
        height (int): the height
        width (int): the width
    """

    def __init__(self, width, height):
        """initializer function

        Args:
            width (int): the width
            height (int): the height
        """
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
