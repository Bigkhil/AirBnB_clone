#!/usr/bin/python3
"""Test Amenity"""
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class Testamenity(unittest.TestCase):
    """
    unittests for Amenity class
    """

    def setUp(self):
        self.model = Amenity()
        self.model_dict = self.model.to_dict()

    def test_instantiation(self):
        self.assertIsInstance(self.model, Amenity)

    def test_attr_empty_string(self):
        self.assertEqual(self.model.name, "")


if __name__ == '__main__':
    unittest.main()
