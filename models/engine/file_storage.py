#!/usr/bin/python3
'''file_storage file serializes and deserializes instances'''
import os
import json


class FileStorage():
    '''file_storage class used for serialization and deserialization'''
    __file_path = './file.json'
    __objects = {}

    def all(self):
        '''return __objects dictionary'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = '{}.{}'.format(obj, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        with open(self.__file_path, 'w') as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        ''' deserializes the JSON file to __objects'''
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                self.__objects = json.loads(file.read())
