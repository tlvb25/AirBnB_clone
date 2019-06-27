#!/usr/bin/python3
"""Module that holds class BaseModel"""
import uuid
from datetime import datetime
import time


class BaseModel:
    """Base class"""

    def __init__(self, *args, **kwargs):
        """Initializes attributes for class BaseModel
        Args:
            id: identification number
        """

        if not kwargs and kwargs != {}:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, time.strptime(v, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ """

        cls = self.__class__.__name__
        return ("[{}] ({}) {}".format(cls, self.id, self.__dict__))

    def save(self):
        """ """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ """

        d = self.__dict__.copy()
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        d['__class__'] = self.__class__.__name__
        return d

    
