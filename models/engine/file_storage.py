#!/usr/bin/python3
'''file_storage file serializes and deserializes instances'''
import json
from models.base_model import BaseModel

class FileStorage():
    '''file_storage class used for serialization and deserialization'''
    __file_path = './file.json'
    __objects = {}

    def all(self):
        '''return __objects dictionary'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        with open(self.__file_path, 'w') as file:
            dict = {}
            for key, value in self.__objects.items():
                dict[key] = value.to_dict()
            json.dump(dict, file)

    def reload(self):
        ''' deserializes the JSON file to __objects'''
        try:
            with open(self.__file_path, "r") as file:
                dictofdicts = json.load(file)
                for key, val in dictofdicts.items():
                    obj = BaseModel(**val)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
