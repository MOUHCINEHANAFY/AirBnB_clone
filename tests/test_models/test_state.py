#!/usr/bin/python3
""" Tests for class State """

import unittest
from models.state import State
from tests.test_models.test_base_model import TestBaseModel


class TestState(TestBaseModel):
    """ Tests for class State """

    def __init__(self, *args, **kwargs):
        """ Inititialize models to test """

        super().__init__(*args, **kwargs)
        self.test_class = State
        self.test_name = 'State'
