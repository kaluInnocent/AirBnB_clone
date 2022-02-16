#!/usr/bin/python3
"""
Test file for city class
"""

import unittest
from models.engine.file_storage import objects
from models.base_model import BaseModel


class TestClass(unittest.TestCase):
    """Test cases"""

    def test_create_instance(self):
        """create a new instance"""
        another_city = BaseModel()
        new_o = objects(another_city.__dict__)
        self.assertIsInstance(new_o, objects)



if __name__ == '__main__':
    unittest.main()
