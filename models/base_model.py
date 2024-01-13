#!/usr/bin/python3
"""Module Base_model"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        kwargs.pop('__class__', None)
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
        """Returns a dictionary containing all keys/values of __dict__."""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict

    def __str__(self):
        """Returns a string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
