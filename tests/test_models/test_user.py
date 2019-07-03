#!/usr/bin/python3
""" Unittest for BaseModel User """
import unittest
from datetime import datetime
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestUser(unittest.TestCase):
    """ Runs Test for User.py """

    def setUp(self):
        """ Sets Up Testing Environment """
        print('set up')
        self.a = User()
        self.a.email = "test@holberton.com"
        self.a.password = "Betty8"
        self.a.first_name = "Betty"
        self.a.last_name = "Holberton"

        self.attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes

    def tearDown(self):
        print('tear down')

    def Test_Instantation(self):
        self.assertIsInstance(self.a, User())

    def Test_Inheriance(self):
        self.assertIsInstance(self.a, BaseModel)

    def Test_attribute(self):
        mark = User()
        for k, v in self.attributes.items():
            self.assertIn(k, self.attributes)
            self.assertEqual(type(getattr(mark, k, None)), v)
    