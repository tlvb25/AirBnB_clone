#!/usr/bin/python3
"""Holds User class that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Initalizes Review class"""

    place_id = ""
    user_id = ""
    text = ""
