#!/usr/bin/python3

import json
from datetime import datetime
from models.user import User


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all serialized objects.
        """
        return self.__objects

    def new(self, obj)
        key = type(obj).__name__ + '.' + obj.id
        FileStorage.__[key] = obj

        def save(self):
            """
            serializes FileStorage.__objects
            """
            with open(FileStorage.__file_path, 'w+') as f:
                dictofobjs = {}
                for key, value in FileStorage.__objects.items():
                    dictofobj[key] = value.to_dict()
                json.dump(dictofobjs, f)

            def reload(self):
                """
                deserialzes instances got from json file
                """
             try:
            with open(FileStorage.__file_path, 'r') as f:
                dictofobjs = json.loads(f.read())
                from models.base_model import BaseModel
                from models.user import User
                for key, value in dictofobjs.items():
                    if value['__class__'] == 'BaseModel'
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif value['__class__'] == 'User':
                        FileStorage.__objects[key] = User(**value)
                   except FileNotFoundError:
        """
        Adds a new object to the storage.

        Args:
            obj: The object to be added.

        Returns:
            None
        """
        key = self.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes objects and saves them to the JSON file.
        """
        json_obj = {}
        for key, value in self.__objects.items():
            if isinstance(value, dict):
                # Value is already a dictionary, use it directly
                json_obj[key] = value
            else:
                try:
                    # Value is assumed to be an instance of BaseModel
                    json_obj[key] = value.to_dict()
                except Exception as e:
                    print(f"Error while converting {value} to dict: {e}")

        with open(self.__file_path, 'w') as f:
            json.dump(json_obj, f)

    def reload(self):
        """
        Deserializes objects from the JSON file.
        """
        try:
            with open(self.__file_path, 'r') as f:
                dictofobjs = json.loads(f.read())
                from models.base_model import BaseModel
                from models.user import User
                for key, value in dictofobjs.items():
                    if value['__class__'] == 'BaseModel':
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif value['__class__'] == 'User':
                        FileStorage.__objects[key] = User(**value)
        except FileNotFoundError:
            pass
