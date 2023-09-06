#!/usr/bin/python3
"""trying to work with unittest module"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """creating series of tests for function"""
    
    def test_instance(self):
        """test whether passed arg is a list"""

        with self.assertRaises(TypeError):
            max_integer("string")
            max_integer(56)
            max_integer((1, 2, 3, 4, 5))

    def test_maxes(self):
        """test for correct output"""

        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([69, 12, 24, 25, 56, 47]), 69)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1, 1, 1, 1, 1,]), 1)
        self.assertEqual(max_integer([9, 8, 7, 6, 5, 4]), 9)
        self.assertEqual(max_integer([1, 3, 2]), 3)
        self.assertEqual(max_integer([]), None)

    def test_values(self):
        """test whether each element is a int"""

        with self.assertRaises(TypeError):
            max_integer([1, 2, "str", 3])
            max_integer([23, (1, 2, 5), 89])

if __name__ == "__main__":
    unittest.main()
