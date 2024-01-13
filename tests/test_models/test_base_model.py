#!/usr/bin/python3
"""test BaseModel"""
import unittest
from datetime import datetime
from models.base_model import BaseModel  # Make sure to replace 'your_module' with the actual name of your module

class TestBaseModel(unittest.TestCase):


    def test_init(self):
        # Test the initialization of BaseModel
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_init_with_arguments(self):
        # Test initialization with arguments
        model_id = "test_id"
        created_at = datetime(2022, 1, 1)
        updated_at = datetime(2022, 2, 2)
        model = BaseModel(id=model_id, created_at=created_at, updated_at=updated_at)
        self.assertEqual(model.id, model_id)
        self.assertEqual(model.created_at, created_at)
        self.assertEqual(model.updated_at, updated_at)

    def test_save(self):
        # Test the save method
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)

    def test_to_dict(self):
        # Test the to_dict method
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

    def test_str(self):
        # Test the string representation
        model = BaseModel()
        str_representation = str(model)
        self.assertIn(model.id, str_representation)
        self.assertIn(model.__class__.__name__, str_representation)

if __name__ == '__main__':
    unittest.main()
