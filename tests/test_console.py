#!/usr/bin/python3
"""Test Console"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest


class TestConsole(unittest.TestCase):
    """Test Console"""

    def test_console(self):
        """Test Console"""

        cityy = City()
        amenityy = Amenity()
        statee = State()
        revieww = Review()
        placee = Place()
        self.assertEqual(cityy.__class__.__name__, "City")
        self.assertEqual(amenityy.__class__.__name__, "Amenity")
        self.assertEqual(statee.__class__.__name__, "State")
        self.assertEqual(revieww.__class__.__name__, "Review")
        self.assertEqual(placee.__class__.__name__, "Place")

    def test_console2(self):
        """
        This test checks if all required classes
        inherit from BaseModel right or not
        """
        cityy = City()
        amenityy = Amenity()
        statee = State()
        revieww = Review()
        placee = Place()
        self.assertTrue(issubclass(cityy.__class__, BaseModel))
        self.assertTrue(issubclass(amenityy.__class__, BaseModel))
        self.assertTrue(issubclass(statee.__class__, BaseModel))
        self.assertTrue(issubclass(revieww.__class__, BaseModel))
        self.assertTrue(issubclass(placee.__class__, BaseModel))


if __name__ == '__main__':
    unittest.main()
