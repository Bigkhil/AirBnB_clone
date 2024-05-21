#!/usr/bin/python3
'''init.py file for package initialization'''
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
