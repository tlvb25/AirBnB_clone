#!/usr/bin/python3
# that serializes instances to a JSON file and deserializes JSON file to instances

from models.base_model import BaseModel
import json
from os import path

class FileStorage:
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
        try:
            with open(self.__file_path, "r") as r:
                dict_of_dicts = json.load(r)
            for k, v in dict_of_dicts.items():
                self.__objects[k] = BaseModel(**v)
        except Exception:
            pass
