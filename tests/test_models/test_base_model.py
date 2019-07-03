#!/usr/bin/python3
"""Unittest for BaseModel class"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Runs tests for base_model.py"""

    def setUp(self):
        """Sets up testing environment"""

        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def test_create(self):
        """Tests the creation of a BaseModel class"""

        self.assertTrue(self.b1)
        self.assertTrue(self.b2)

    def test_id_check(self):
        """Checks for ID and compares them"""

        self.assertNotEqual(self.b1.id, self.b2.id)

    def test_attr_check(self):
        """Checks for user created attributes"""

        self.b1.name = "Marc"
        self.b2.name = "Tywan"
        self.assertEqual(self.b1.name, "Marc")
        self.assertEqual(self.b2.name, "Tywan")
        self.assertNotEqual(self.b1.name, self.b2.name)

    def test_toDict(self):
        """Checks output when using to_dict()"""

        self.assertFalse("__class__" in self.b1.__dict__)
        self.assertFalse("__class__" in self.b2.__dict__)
        dict_check = self.b1.to_dict()
        self.assertTrue("__class__" in dict_check)
        self.assertFalse("__class__" in self.b2.__dict__)

    def test_change_name(self):
        """Checks you can change the name"""

        self.b1.name = "Marc"
        self.b2.name = "Tywan"
        self.b1.name = "Rhulad"
        self.assertTrue(self.b1.name, "Rhulad")
        self.assertTrue(self.b2.name, "Tywan")

    def test_compare_create_and_update(self):
        """Makes sure create and update are slightly different"""

        self.assertNotEqual(self.b1.created_at, self.b1.updated_at)

    def test_updateAt_updates(self):
        """Makes sure updated_at updates"""

        tmp = self.b1.updated_at
        self.b1.save()
        self.assertNotEqual(tmp, self.b1.updated_at)

    def test_id_length(self):
        """Checks to make sure id is the right amount of characters"""

        self.assertTrue(len(self.b1.id), 36)
        self.assertTrue(len(self.b2.id), 36)

    def test_user_attr(self):
        """Checks to see if a user created attribute is updated"""

        self.assertFalse("number" in self.b1.__dict__)
        self.assertFalse("number" in self.b2.__dict__)
        self.b1.number = 22
        self.assertTrue("number" in self.b1.__dict__)
        self.assertFalse("number" in self.b2.__dict__)

    def test_to_dict(self):
        """Tests the to_dict() method"""

        self.assertEqual(dict, type(self.b1.to_dict()))

    def test_to_dict_contents(self):
        """Tests that the correct keys are being added to to_dict()"""

        self.assertIn("created_at", self.b1.to_dict())
        self.assertIn("updated_at", self.b1.to_dict())
        self.assertIn("__class__", self.b1.to_dict())
        self.assertNotIn("name", self.b1.to_dict())
        self.b1.name = "Marc"
        self.assertIn("name", self.b1.to_dict())

    def test_two_dicts_one_instance(self):
        """Makes sure to_dict() and __dict__ are not equal"""

        self.assertNotEqual(self.b1.to_dict(), self.b1.__dict__)

    def tearDown(self):
        """Breaks down the testing environment"""

        pass
