#!/usr/bin/python3
""" Tests for class User """

import unittest
from models.user import User
from tests.test_models.test_base_model import TestBaseModel


class TestUser(TestBaseModel):
    """ Tests for class User """

    def __init__(self, *args, **kwargs):
        """ Inititialize models to test """

        super().__init__(*args, **kwargs)
        self.test_class = User
        self.test_name = 'User'
