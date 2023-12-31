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
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
