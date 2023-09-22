#!/usr/bin/python3
"""unit tests for base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

b1 = Base()
b2 = Base()
b3 = Base(98)
b4 = Base()
b5 = Base()


class Test_Base(unittest.TestCase):
    """running tests for base class"""
    
    def test_instance_attr(self):
        """test if id is properly assigned"""
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 98)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, 4)

    def test_private_attr(self):
        b1 = Base()
        with self.assertRaises(AttributeError):
            print(b1.__nb_objects)
    
    def test_static_to_json_string(self):
        self.assertEqual(b1.to_json_string([]), "[]")
        self.assertEqual(b2.to_json_string(None), "[]")

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"id": 12, "width": 10, \
"height": 7, "x": 2, "y": 8}]')
        self.assertIsInstance(json_dictionary, str)

        json_dictionary = Base.to_json_string([dictionary,
            dictionary, dictionary])
        self.assertEqual(json_dictionary,
'[{"id": 12, "width": 10, "height": 7, "x": 2, "y": 8}, \
{"id": 12, "width": 10, "height": 7, "x": 2, "y": 8}, \
{"id": 12, "width": 10, "height": 7, "x": 2, "y": 8}]')
        self.assertIsInstance(json_dictionary, str)


if __name__ == "__main__":
    unittest.main()
