#!/usr/bin/python3
"""
Defines the state module
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Blueprint for amenity objects
    """
    name = ""
