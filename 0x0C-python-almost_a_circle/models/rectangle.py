#!/usr/bin/python3
"""class for rectangle a subclass of base"""
import base


class Rectangle(base.Base):
    """class about a retangle that inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer for rectangle class

        Args:
            width: width if rectangle
            height: height of rectangle
            x: axis positon of rectangle
            y: axis position of rectangle
            id: for inheritance
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """getter method for width

        setter method validates param
        """
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """getter method for height

        setter method validates param
        """
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """getter method for x

        setter will validate params
        """
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getter method for y

        setter will check param
        """
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """calculate area of retangle

        Return:
            area of rectangle instance
        """
        return self.width * self.height

    def display(self):
        """prints the rectangle using '#' char"""
        print("{}".format('\n' * self.y), end='')
        for i in range(self.height):
            print(f"{' ' * self.x}{'#' * self.width}")

    def __str__(self):
        """string of rect

        Returns:
            string repr of the rect
        """
        return f"[Rectangle] ({self.id}) {self.x:d}/{self.y:d} \
- {self.width:d}/{self.height:d}"

    def update(self, *args, **kwargs):
        """assigns what is in args to instance attrs

        Args:
            args: like a list of vals to assign in order
            kwargs: dict of jey word arguments
        """
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            if i == 1:
                self.width = args[i]
            if i == 2:
                self.height = args[i]
            if i == 3:
                self.x = args[i]
            if i == 4:
                self.y = args[i]

        if len(args) > 0:
            return

        for i, v in kwargs.items():
            if hasattr(self, i):
                setattr(self, i, v)

    def to_dictionary(self):
        """makes dict for instance

        Returns:
            dict of instance
        """
        keys = ("id", "width", "height", "x", "y")
        d_rep = dict()
        for i in keys:
            d_rep[i] = getattr(self, i, 0)

        return d_rep
