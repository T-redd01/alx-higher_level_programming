#!/usr/bin/python3
"""load from json file"""
import json


def load_from_json_file(filename):
    """loads from file

    Args:
        filename: name of file
    """
    with open(filename, "r") as f:
        string = f.read()
        obj = json.loads(string)
        return obj
