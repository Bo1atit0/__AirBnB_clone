#!/usr/bin/python3
"""
test file for the filestorage class
"""
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class Test_filestorage(unittest.TestCase):
  """
  Testing the filestorage class and it's methods
  """

  def setUp(self):
    """
    create a FileStorage object to be tested
    """
    self.file_storage = FileStorage()

  def tearDown(self):
    """
    delete the FileStorage object
    """
    del self.file_storage

  def test_all(self):
    """
    test the all() method
    """
    self.assertIsInstance(self.file_storage.all(), dict)
    #self.assertEqual(self.file_storage.all(), self.file_storage.FileStorage.__objects)

  def test_new(self):
    """
    test the new() method
    """
    new_obj = BaseModel()
    self.file_storage.new(new_obj)
    key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
    new_dict = self.file_storage.all()
    self.assertIn(key, new_dict)


if '__name__ ' == '__main__':
  unittest.main()
