#!/usr/bin/python3
"""Holds User class that inherits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = int(0)
    max_guest = int(0)
    price_by_night = int(0)
    latitude = float(0.0)
    longitude = float(0.0)
    amenity_ids = []
