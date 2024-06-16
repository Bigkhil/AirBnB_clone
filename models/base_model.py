#!/usr/bin/python3
'''this is the base model for all the classes'''
import uuid
from datetime import datetime


class BaseModel():
    '''this is the base class for all classes'''
    def __init__(self, *args, **kwargs):
        '''constructor for class instances'''
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    pass
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        '''returns string to display when printing the instances'''
        return ("[{}] ({}) {}".
                format(BaseModel.__name__, self.id, self.__dict__))

    def save(self):
        '''updates the public instance attribute updated_at'''
        from models import storage
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        dict = self.__dict__
        dict['__class__'] = BaseModel.__name__
        if not type(self.created_at) is str:
            dict['created_at'] = self.created_at.isoformat()
        if not type(self.updated_at) is str:
            dict['updated_at'] = self.updated_at.isoformat()
        return dict
