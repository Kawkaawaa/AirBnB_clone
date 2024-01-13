import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create an instance of FileStorage for testing
        cls.file_path = "test_file.json"
        cls.storage = FileStorage()
        cls.storage._FileStorage__file_path = cls.file_path

    @classmethod
    def tearDownClass(cls):
        # Clean up: Remove the test file after all tests are done
        if os.path.exists(cls.file_path):
            os.remove(cls.file_path)

    def setUp(self):
        # Clear the objects in FileStorage before each test
        self.storage._FileStorage__objects = {}

    def test_all_empty_storage(self):
        # Test the all method on an empty storage
        result = self.storage.all()
        self.assertEqual(result, {})

    def test_all_non_empty_storage(self):
        # Test the all method on a non-empty storage
        obj = BaseModel()
        self.storage.new(obj)
        result = self.storage.all()
        self.assertEqual(result, {"BaseModel." + obj.id: obj})

    def test_new_method(self):
        # Test the new method
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(self.storage.all(), {"BaseModel." + obj.id: obj})

    def test_save_and_reload(self):
        # Test saving and reloading objects
        obj1 = BaseModel()
        obj1.name = "Object1"
        self.storage.new(obj1)
        self.storage.save()

        # Create a new instance of FileStorage for reloading
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

        # Check if the reloaded storage contains the saved object
        result = new_storage.all()
        self.assertEqual(result, {"BaseModel." + obj1.id: obj1})

    def test_save_existing_file(self):
        # Test saving to an existing file
        obj1 = BaseModel()
        obj1.name = "Object1"
        self.storage.new(obj1)
        self.storage.save()

        obj2 = BaseModel()
        obj2.name = "Object2"
        self.storage.new(obj2)
        self.storage.save()  # This should overwrite the existing file

        # Create a new instance of FileStorage for reloading
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

        # Check if the reloaded storage contains both objects
        result = new_storage.all()
        expected_result = {
            "BaseModel." + obj1.id: obj1,
            "BaseModel." + obj2.id: obj2
        }
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
