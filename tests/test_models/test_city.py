#!/usr/bin/python3
"""
Test file for city class
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestClass(unittest.TestCase):
    """Test cases"""

    def setUp(self):
        self.city = City()
        return super().setUp()

    def tearDown(self):
        del(self.city)
        return super().tearDown()

    def test_create_instance(self):
        """create a new instance"""
        self.assertIsInstance(self.city, City)

    def test_create_isinstance_check_parent(self):
        """ check ifi its instance of parent"""
        self.assertIsnstance(self.city, BaseModel)

    def test_class_attribute(self):
        """initialise classs attribute"""
        self.city.name = "Abeokuta"
        self.assertIs(self.city.name, 'Abeokuta')

    def test_parent_of_city(self):
        """ check if city is parent of BaseModel"""
        self.assertEqual(isinstance(self.city, BaseModel), True)


if __name__ == '__main__':
    unittest.main()
