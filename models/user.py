#!/usr/bin/python3
"""Holds User class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that defines User information"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
