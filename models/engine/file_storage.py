#!/usr/bin/python3
# that serializes instances to a JSON file and deserializes JSON file to instances

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

import json
from os import path

class FileStorage:
    """Class to hold information and saved instances"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        tmp_dict = {}
        for k, v in self.__objects.items():
            tmp_dict[k] = v.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as written_file:
            json.dump(tmp_dict, written_file)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file (__file_path) """
        dict_of_dicts = {}
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review}
            
        try:
            temp_dict = {}
            with open(self.__file_path, "r") as r:
                dict_of_dicts = json.load(r)
            for k, v in dict_of_dicts.items():
                if v['__class__'] in classes:
                    temp_dict[k] = classes[v['__class__']](**v)
            self.__objects=temp_dict
        except Exception:
            pass
