#!/usr/bin/python3
"""class for rectangle with init"""


class Rectangle:
    """class about rectangle"""

    def __init__(self, width=0, height=0):
        """initialize the rectanle instance

        Args:
            width (int): width of rect
            height (int): height of rect
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method for rect width

        setter method validates parameter
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method for rect height

        setter will validate parameter
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate area of rect"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate primeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width*2 + self.__height*2

    def __str__(self):
        """printable string of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        r_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                r_str += "#"
            if self.__height - 1 != i:
                r_str += '\n'
        return r_str

    def __repr__(self):
        """representation of rect class object"""
        return f"<3-rectangle.Rectangle object at {id(self):x}"
