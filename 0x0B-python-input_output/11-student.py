#!/usr/bin/python3
"""class students"""


class Student:
    """class about students

    Attributes:
        first_name (str): first name
        last_name (str): last name
        age (int): student age
    """

    def __init__(self, first_name, last_name, age):
        """Initializer for student

        Args:
            first_name: first name
            last_name: last name
            age: student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dict repr of class for json"""
        if attrs == None or not isinstance(attrs, list):
            return self.__dict__

        new = dict()
        for i in attrs:
            try:
                ats = getattr(self, i)
            except Exception:
                pass
            else:
                k_v = (i, ats)
                new.update((k_v,))
        return new

    def reload_from_json(self, json):
        """replace attrs

        Args:
            json (dict): to change attrs
        """
        self.__dict__ = json
