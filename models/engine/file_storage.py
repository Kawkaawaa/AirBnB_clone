
#!/usr/bin/python3

import json
from models


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objetcs

    def new(self, obj):
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

                   except FileNotFoundError:
            pass
