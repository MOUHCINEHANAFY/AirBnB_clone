#!/usr/bin/python3
""" Tests for class Place """

import unittest
from models.place import Place
from tests.test_models.test_base_model import TestBaseModel


class TestPlace(TestBaseModel):
    """ Tests for class Place """

    def __init__(self, *args, **kwargs):
        """ Inititialize models to test """

        super().__init__(*args, **kwargs)
        self.test_class = Place
        self.test_name = 'Place'
