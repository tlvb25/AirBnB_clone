#!/usr/bin/python3
""" Unittest for BaseModel User """
import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """ Runs Test for User.py """

    def setUp(self):
        """ Sets Up Testing Environment """
        self.a = User()
        self.a.email = "test@holberton.com"
        self.a.password = "Betty8"
        self.a.first_name = "Betty"
        self.a.last_name = "Holberton"

    def Test_Instantation(self):
        self.assertIsInstance(self.a, User())

    def Test_Inheriance(self):
        self.assertIsInstance(self.a, BaseModel)

    def Test_attribute(self):
        self.