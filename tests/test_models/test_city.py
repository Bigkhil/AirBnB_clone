#!/usr/bin/python3
"""Test city"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest


class Testcity(unittest.TestCase):
    """
    unittests for city class
    """

    def setUp(self):
        self.model = City()
        self.model_dict = self.model.to_dict()

    def test_instantiation(self):
        self.assertIsInstance(self.model, City)

    def test_attr_empty_string(self):
        self.assertEqual(self.model.state_id, "")
        self.assertEqual(self.model.name, "")


if __name__ == '__main__':
    unittest.main()
