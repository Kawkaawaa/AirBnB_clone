#!/usr/bin/python3
"""
Defines the state module
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    Bluerint for City objects
    """
    state_id = ""
    name = ""
