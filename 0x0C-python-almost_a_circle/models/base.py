#!/usr/bin/python3
"""Base class or parent class to inherit from"""
import json
import csv


class Base:
    """parent class for other classes

    Attributes:
        __nb_objects: counts number of objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer for this class

        Args:
            id: number assigned to instance
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that gets json repr of dicts

        Args:
            list_dictionaries: list of dictionaries

        Returns:
            list with json string repr of dicts
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to json file list_objs

        Args:
            list_objs: list of instances
        """
        name = cls.__name__ + ".json"
        holder = []
        for i in list_objs:
            holder.append(i.to_dictionary())

        with open(name, 'w') as f:
            f.write(cls.to_json_string(holder))

    @staticmethod
    def from_json_string(json_string):
        """makes object from json string

        Args:
            json_string: string for making obj

        Returns:
            obj made from string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create an instance with attribute values in dictionary

        Args:
            dictionary: values for attributes

        Returns:
            instance with attributes in dictionary
        """
        bob = cls(1, 1)
        bob.update(**dictionary)
        return bob

    @classmethod
    def load_from_file(cls):
        """make instances from a file"""
        name = cls.__name__ + ".json"
        objs = []
        try:
            with open(name, 'r') as f:
                my_l = cls.from_json_string(f.read())
                for i in my_l:
                    objs.append(cls.create(**i))
        except FileNotFoundError:
            return []
        return objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save in csv format

        Args:
            list_objs: list of objects
        """
        name = cls.__name__ + ".csv"
        data = []
        header = []
        if cls.__name__ == "Rectangle":
            header = ["id", "width", "height", "x", "y"]
            for i in list_objs:
                row = []
                for j in header:
                    row.append(getattr(i, j))
                data.append(row)

        if cls.__name__ == "Square":
            header = ["id", "size", "x", "y"]
            for i in list_objs:
                row = []
                for j in header:
                    row.append(getattr(i, j))
                data.append(row)
        with open(name, 'w') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(header)
            csvwriter.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """loads objs from file"""
        name = cls.__name__ + ".csv"
        objs = []
        with open(name, 'r') as f:
            csvreader = csv.reader(f)
            header = next(csvreader)
            for i in csvreader:
                bob = cls.create()
                for j in range(len(header)):
                    setattr(bob, header[j], int(i[j]))
                objs.append(bob)
        return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws square with turtle graphics

        Args:
            list_rectangle: list of rectangles
            list_squares: list of squares
        """
        window = turtle.Screen()
        window.bgcolor("black")
        p = turtle.Turtle()
        p.pensize(5)
        p.color("lightgreen")
        for i in list_rectangles:
            coords = (
                    getattr(i, "width"),
                    getattr(i, "height"),
                    getattr(i, "width"),
                    getattr(i, "height")
                    )
            for j in coords:
                p.forward(j)
                p.left(90)

        for i in list_squares:
            size = getattr(i, "size")
            for i in range(4):
                p.forward(size)
                p.left(90)
