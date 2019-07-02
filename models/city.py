#!/usr/bin/python3
"""Holds User class that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Initializes the City class"""

    state_id = ""
    name = ""
