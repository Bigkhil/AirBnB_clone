#!/usr/bin/python3
'''this is the base model for all the classes'''
import uuid
import datetime


class BaseModel():
    '''this is the base class for all classes'''
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.date()
