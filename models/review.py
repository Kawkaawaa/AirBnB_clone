#!/usr/bin/python3
"""
Defines the state model
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    Blueprint for Review objects
    """
    place_id = ""
    user_id = ""
    text = ""
