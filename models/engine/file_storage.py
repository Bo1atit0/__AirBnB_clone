#!/usr/bin/python3

"""
a class FileStorage that serializes instances to a JSON file 
and deserializes JSON file to instances
"""
from models.base_model import BaseModel
import json

class FileStorage:
  """
  a class that serializes and deserializes instances to and from a JSON file
  """
  __file_path = "file.json"
  __objects = {}

  def all(self):
    """
    returns the dictionary __objects
    """
    return self.__objects

  def new(self, obj):
    """
    sets in 'obj' in __objects with key <obj class     
    name>.id
    """
    key = "{}.{}".format(obj.__class__.__name__, obj.id)
    self.__objects[key] = obj

  def save(self):
    """
    serializes __objects to the JSON file
    """
    
    

  
  