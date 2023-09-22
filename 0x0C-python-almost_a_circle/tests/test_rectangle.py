#!/usr/bin/python3
"""unit tests for rectangle class"""
import unittest
from models.rectangle import Rectangle

r1 = Rectangle(10, 2)
r2 = Rectangle(26, 33, 1, 4, 98)
r3 = Rectangle(4, 5, 6, 7)
r4 = Rectangle(8, 9, 5)


class Test_Rectangle(unittest.TestCase):
    """test cases for rectangle class"""

    def test_assignment(self):
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 5)

        self.assertEqual(r2.width, 26)
        self.assertEqual(r2.height, 33)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 4)
        self.assertEqual(r2.id, 98)

        self.assertEqual(r3.width, 4)
        self.assertEqual(r3.height, 5)
        self.assertEqual(r3.x, 6)
        self.assertEqual(r3.y, 7)
        self.assertEqual(r3.id, 6)

        self.assertEqual(r4.width, 8)
        self.assertEqual(r4.height, 9)
        self.assertEqual(r4.x, 5)
        self.assertEqual(r4.y, 0)
        self.assertEqual(r4.id, 7)

    def test_raise_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = "string"
            r1.width = 2.36
            r1.width = [1, 2, 3]

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r2.height = "string"
            r2.height = 3.142
            r2.height = [1, 2, 3]

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r3.x = "string"
            r3.x = 3.1425
            r3.x = (1, 2, 3)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r4.y = "string"
            r4.y = 9.56
            r4.y = {1, 2, 3}

    def test_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.width = 0
            r1.width = -5

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r2.height = 0
            r2.height = -9

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r3.x = -1

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r4.y = -2

    def test_area(self):
        self.assertEqual(r1.area(), 20)
        self.assertEqual(r2.area(), 858)
        self.assertEqual(r3.area(), 20)
        self.assertEqual(r4.area(), 72)

    def test_str(self):
        self.assertEqual(str(r1), "[Rectangle] (5) 0/0 - 10/2")
        self.assertEqual(str(r2), "[Rectangle] (98) 1/4 - 26/33")
        self.assertEqual(str(r3), "[Rectangle] (6) 6/7 - 4/5")
        self.assertEqual(str(r4), "[Rectangle] (7) 5/0 - 8/9")

    def test_update_args(self):
        r1.update(1)
        self.assertEqual(r1.id, 1)

        r1.update(1, 2)
        self.assertEqual(r1.width, 2)

        r1.update(1, 2, 3)
        self.assertEqual(r1.height, 3)

        r1.update(1, 2, 3, 4)
        self.assertEqual(r1.x, 4)

        r1.update(1, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

        r1.update(1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(str(r1), "[Rectangle] (1) 4/5 - 2/3")

    def test_update_kwargs(self):
        r2.update(id = 2, width = 2, height = 3, x = 4, y = 5)
        self.assertEqual(str(r2), "[Rectangle] (2) 4/5 - 2/3")

        my_dict = {"id" : 3, "height" : 4, "x" : 5, "y" : 6, "width" : 7}
        r3.update(**my_dict)
        self.assertEqual(str(r3), "[Rectangle] (3) 5/6 - 7/4")

        my_dict = {"id" : 3, "height" : 4, "x" : 5, "y" : 6,
                "width" : 7, "ran" : 98, "attr" : 29}
        r3.update(**my_dict)
        self.assertEqual(str(r3), "[Rectangle] (3) 5/6 - 7/4")

    def test_update_choose_args(self):
        my_dict = {"id" : 3, "height" : 4, "x" : 5, "y" : 6, "width" : 7}
        args = (4, 2, 3, 4, 5)
        r4.update(*args, **my_dict)
        self.assertEqual(str(r4), "[Rectangle] (4) 4/5 - 2/3")

    def test_to_dict(self):
        self.assertEqual(r1.to_dictionary(), {"id" : 5, "x" : 0, "y" : 0,
            "width" : 10, "height" : 2})
        r2.height = 4
        self.assertEqual(r2.to_dictionary(), {"id" : 98, "x" : 1, "y" : 4,
            "width" : 26, "height" : 4})

if __name__ == "__main__":
    unittest.main()
