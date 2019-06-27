#!/usr/bin/python3
"""Module that holds class BaseModel"""
import uuid
import datetime


class BaseModel:
    """Base class"""

    def __init__(self, *args, **kwargs):
        """Initializes attributes for class BaseModel
        Args:
            id: identification number
        """

        if not kwargs and kwargs != {}:
            for k, v in kwargs.items():
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ """

        cl = self.__class__.__name__
        return ("[{}] ({}) {}".format(cl, self.id, self.__dict__))

    def save(self):
        """ """

        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ """

        d = self.__dict__.copy()
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d

    
