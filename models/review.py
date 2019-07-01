#!/usr/bin/python3
"""Holds User class that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
