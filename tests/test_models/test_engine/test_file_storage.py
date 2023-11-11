#!/usr/bin/python3
""" Tests for class FileStorage """

import unittest
from models.engine.file_storage import FileStorage
import json
import os
import os.path


class TestFileStorage(unittest.TestCase):
    """ Tests for class FileStorage """

    def remove_file(self):
        """ Removes Json file after tests """
        if os.path.exists('save.json'):
            os.remove('save.json')

    def test_file_path(self):
        """ Tests file path to be json file """
        pass

    def test_all(self):
        """ Tests dictionary objects """
        pass

    def test_new(self):
        """ Tests setting new object with key """
        pass

    def test_save(self):
        """ Tests serializing objects to json file """
        pass

    def test_reload(self):
        """ Tests deserializing the json file """
        pass
