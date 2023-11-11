#!/usr/bin/python3
""" Tests for class City """

import unittest
from models.city import City
from tests.test_models.test_base_model import TestBaseModel


class TestCity(TestBaseModel):
    """ Tests for class City """

    def __init__(self, *args, **kwargs):
        """ Inititialize models to test """

        super().__init__(*args, **kwargs)
        self.test_class = City
        self.test_name = 'City'
