#!/usr/bin/python3
"""Test User"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import unittest


class Testuser(unittest.TestCase):
    """Unittest for testing the User class."""

    def setUp(self):
        self.model = User()
        self.model_dict = self.model.to_dict()

    def test_instantiation(self):
        self.assertIsInstance(self.model, User)

    def test_attr_empty_string(self):
        self.assertEqual(self.model.email, "")
        self.assertEqual(self.model.password, "")
        self.assertEqual(self.model.first_name, "")
        self.assertEqual(self.model.last_name, "")


if __name__ == '__main__':
    unittest.main()
