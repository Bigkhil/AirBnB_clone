#!/usr/bin/python3
"""Test state"""

from models.base_model import BaseModel
from models.state import State
import unittest


class Teststate(unittest.TestCase):
    """
    unittests for state class
    """

    def setUp(self):
        self.model = State()
        self.model_dict = self.model.to_dict()

    def test_instantiation(self):
        self.assertIsInstance(self.model, State)

    def test_attr_empty_string(self):
        self.assertEqual(self.model.name, "")


if __name__ == '__main__':
    unittest.main()
