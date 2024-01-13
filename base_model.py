#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    def _init_(self, *args, **kwargs):
        kwargs.pop('_class_', None)
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Updates the attribute updated_at with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of _dict_."""
        instance_dict = self._dict_.copy()
        instance_dict['_class'] = self.class.name_
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict

    def _str_(self):
        """Returns a string representation of the instance."""
        return f"[{self._class.name}] ({self.id}) {self.dict_}"

