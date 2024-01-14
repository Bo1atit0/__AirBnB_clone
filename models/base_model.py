#!/usr/bin/python3

import uuid
from datetime import datetime
import models 
"""
a class BaseModel that defines all common attributes/methods for other classes
"""


class BaseModel:
  """
  a BaseModel class
  """

  def __init__(self, *args, **kwargs):
    """
    initializes the BaseModel class
    *args: won't be used
    """
    if kwargs:
      for key, value in kwargs.items():
        if key != '__class__':
          if key in ['created_at', 'updated_at']:
            setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
          else:
            setattr(self, key, value)
    else:
      self.id = str(uuid.uuid4())
      self.created_at = datetime.now()
      self.updated_at = datetime.now()

  def __str__(self):
    """
    returns the string representation of an instance
    """
    return "[{}] ({}) {}".format(self.__class__.__name__,     self.id, self.__dict__)

  def save(self):
    """
    updates the updated_at attribute with the current datetime
    """
    self.updated_at = datetime.now()

  def to_dict(self):
    """
    returns a dictionary containing all keys/values of __dict__ of the instance
    """
    
    obj_dict = self.__dict__.copy()
  
    obj_dict["__class__"] = self.__class__.__name__
    obj_dict["created_at"] = self.created_at.isoformat()
    obj_dict["updated_at"] = self.updated_at.isoformat()
    return obj_dict
  