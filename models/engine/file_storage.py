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
#        self.__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):

        tmp_dict = {}
        for k in self.__objects:
            tmp_dict[k] = self.__objects[k].to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as written_file:
            json.dump(tmp_dict, written_file)

    def reload(self):

        tmp = {}
        try:
            with open(self.__file_path, "r") as r:
                tmp = json.load(r)
            for k, v in tmp.items():
                self.__objects[k] = BaseModel(**v)
        except Exception:
            pass


        '''
        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as r:
                return json.load(r)
        '''
        '''
        try:
            print("hello")
            with open(self.__file_path, "r") as read_file:
                x = json.load(read_file)
            return x
        except Exception:
            print("goodbye")
            pass
        '''
#            with open(self.__file_path, mode='r') as read_file:
 #               return json.load(read_file)
