#!/usr/bin/python3
""" unittest for square testing file """
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class SquareTestCase(unittest.TestCase):
    """ class for square testing flie """

    def setUp(self):
        """
        method for Resets id
        """
        Base._Base__nb_objects = 0

    def test_square_id_increment(self):
        pass


if __name__ == '__main__':
    unittest.main()
