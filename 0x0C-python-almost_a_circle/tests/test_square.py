#!/usr/bin/python3
"""unit tests for square class"""
import unittest
from models.square import Square

s1 = Square(5)
s2 = Square(6, 8)
s3 = Square(7, 3, 2)
s4 = Square(8, 5, 6, 98)


class Test_Square(unittest.TestCase):
    """tests for square class"""
    
    def test_assignment(self):
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 8)

        self.assertEqual(s2.width, 6)
        self.assertEqual(s2.height, 6)
        self.assertEqual(s2.x, 8)
        self.assertEqual(s2.y, 0)
        self.assertEqual(s2.id, 9)

        self.assertEqual(s3.width, 7)
        self.assertEqual(s3.height, 7)
        self.assertEqual(s3.x, 3)
        self.assertEqual(s3.y, 2)
        self.assertEqual(s3.id, 10)

        self.assertEqual(s4.width, 8)
        self.assertEqual(s4.height, 8)
        self.assertEqual(s4.x, 5)
        self.assertEqual(s4.y, 6)
        self.assertEqual(s4.id, 98)

    def test_str(self):
        self.assertEqual(str(s1), "[Square] (8) 0/0 - 5")
        self.assertEqual(str(s2), "[Square] (9) 8/0 - 6")
        self.assertEqual(str(s3), "[Square] (10) 3/2 - 7")
        self.assertEqual(str(s4), "[Square] (98) 5/6 - 8")

    def test_size_get_set(self):
        self.assertEqual(s1.size, 5)

        s1.size = 10
        self.assertEqual(s1.size, 10)

        s1.size = 5
        self.assertEqual(s1.size, 5)

    def test_assigment_type_errs(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.size = "string"
            s1.size = (1, 2, 3)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s2.x = "string"
            s2.x = {"g" : 4, "5" : 5}

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s3.y = [1, 2, 3]
            s3.y = "str"

    def test_assignment_value_errs(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.size = 0
            s1.size = -1

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s2.x = -69

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s3.y = -5

    def test_update(self):
        s1.update(1, 5, 0, 0)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s2.update(2, 8, 1, 2, 5, 6)
        self.assertEqual(str(s2), "[Square] (2) 1/2 - 8")

        kwarg = {"size": 6, "y" : 2, "id" : 3}
        s3.update(**kwarg)
        self.assertEqual(str(s3), "[Square] (3) 3/2 - 6")

        s4.update(id=4)
        self.assertEqual(s4.id, 4)

        s4.update(4, 9, 4, 6, **kwarg)
        self.assertEqual(str(s4), "[Square] (4) 4/6 - 9")

    def test_to_dictionary(self):
        self.assertEqual(s1.to_dictionary(), {"id" : 8, "x" : 0, "y" : 0,
            "size" : 5})

        s2.size = 8
        self.assertEqual(s2.to_dictionary(), {"x" : 8, "y" : 0,
            "id" : 9, "size" : 8})

if __name__ == "__main__":
    unittest.main()
