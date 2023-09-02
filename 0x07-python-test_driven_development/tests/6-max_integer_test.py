#!/usr/bin/python3
"""trying to work with unittest module"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """creating series of tests for function"""

    """
    What tests to be done:
        - paramter must be a list
        - list must contain only integers
        - 
