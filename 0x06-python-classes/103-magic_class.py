#!/usr/bin/python3
"""for bytecode checking"""
import math


class MagicClass:
    """Class to decompile

    Attributes:
        _MagicClass__radius (int): radius of object
    """

    def __init__(self, radius):
        """Initialize magic class

        Args:
            radius (int): radius of instance
        """
        self._MagicClass__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self._MagicClass__radius = radius

    def area(self):
        """get area of circle ?

        Returns:
            area of circle
        """
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """get circumference of circle

        Returns:
            circumference of circle
        """
        return 2 * math.pi * self._MagicClass__radius
