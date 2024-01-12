#!/usr/bin/python3

import json


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

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj: The object to be added.

        Returns:
            None
        """
        key = self._class.name_ + "." + str(obj.id)
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
                file_content = f.read().strip()
                if file_content:
                    dict_of_objs = json.loads(file_content)
                    self.__objects = dict_of_objs
                # Additional logic to reconstruct objects from the dictionary
        except FileNotFoundError:
            pass
