#!/usr/bin/python3
"""Test review"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest


class Testreview(unittest.TestCase):
    """
    unittests for Review class
    """

    def test_class(self):
        """
        Tests if the class is named correctly.
        """

    def setUp(self):
        self.model = Review()
        self.model_dict = self.model.to_dict()

    def test_instantiation(self):
        self.assertIsInstance(self.model, Review)

    def test_attr_empty_string(self):
        self.assertEqual(self.model.place_id, "")
        self.assertEqual(self.model.user_id, "")
        self.assertEqual(self.model.text, "")


if __name__ == '__main__':
    unittest.main()
