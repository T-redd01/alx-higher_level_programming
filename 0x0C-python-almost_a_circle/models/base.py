#!/usr/bin/python3
"""Base class or parent class to inherit from"""
import json


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
        print(name)
        holder = []
        for i in list_objs:
            holder.append(i.to_dictionary())

        with open(name, 'w') as f:
            f.write(to_json_string(holder))

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
        bob = cls(0, 0)
        bob.update(dictionary)
        return bob

    @classmethod
    def load_from_file(cls):
        """make instances from a file"""
        name = cls.__name__ + ".json"
        objs = []
        try:
            with open(name, 'r') as f:
                for line in f:
                    objs.append(create(from_json_string(line)))
        except FileNotFoundError:
            return []
        return objs
