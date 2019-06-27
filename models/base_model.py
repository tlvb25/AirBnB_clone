#!/usr/bin/python3
"""Module that holds class BaseModel"""
import uuid
import datetime


class BaseModel:
    """Base class"""

    def __init__(self, id, created_at, updated_at):
        """Initializes attributes for class BaseModel
        Args:
            id: identification number
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ """

        cls = self.__class.__name
        return ("[{}] ({}) {}".format(cls, self.id, self.__dict__)

    def save(self):
        """ """

        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ """

        d = {"__class__": BaseModel, "self.id":
