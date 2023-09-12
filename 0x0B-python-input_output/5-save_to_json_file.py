#!/uar/bin/python3
"""saving to file"""
import json


def save_to_json_file(my_obj, filename):
    """saving to file

    Args:
        my_obj: object to write
        filename: file to write to
    """
    with open(filename, "w") as f:
        string = json.dumps(my_obj)
        f.write(string)
