#!/usr/bin/python3
"""Module that holds class BaseModel"""
import uuid
import datetime


class BaseModel:
    """Base class"""

    def __init__(self, id=None, created_at=None, updated_at=None):
        """Initializes attributes for class BaseModel
        Args:
            id: identification number
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ """

        cls = self.__class.__name__
        return ("[{}] ({}) {}".format(cls, self.id, self.__dict__))

    def save(self):
        """ """

        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ """

        d = self.__dict__.copy
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d
