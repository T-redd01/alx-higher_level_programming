#!/usr/bin/python3
"""class for square which inherits from rectangle"""
import rectangle


class Square(rectangle.Rectangle):
    """indirectly inherits from base and directly from rect"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializer for square using rects getter, setter

        Args:
            size: width and height of square
            x: axis val for x
            y: axis val for y
            id: class attrbute
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for square size

        setter will set height and width with validation
        """
        return self.width

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def __str__(self):
        """string repr of square

        Returns:
            string for square, overloads rect, is this polymorphism
        """
        return f"[Square] ({self.id}) {self.x:d}/{self.y:d} - {self.width:d}"

    def update(self, *args, **kwargs):
        """updates instance attributes

        Args:
            args: list of values to assign
            kwargs: dict of values to assign with key names
        """
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            if i == 1:
                self.size = args[i]
            if i == 2:
                self.x = args[i]
            if i == 3:
                self.y = args[i]

        if len(args) > 0:
            return

        for i, v in kwargs.items():
            if hasattr(self, i):
                setattr(self, i, v)

    def to_dictionary(self):
        """create dict repr of square

        Returns:
            square instance as a dict
        """
        keys = ("id", "size", "x", "y")
        d_rep = dict()
        for i in keys:
            d_rep[i] = getattr(self, i, 0)
        return d_rep
