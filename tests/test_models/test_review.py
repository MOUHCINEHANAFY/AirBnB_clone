#!/usr/bin/python3
""" Tests for class Review """

import unittest
from models.review import Review
from tests.test_models.test_base_model import TestBaseModel


class TestReview(TestBaseModel):
    """ Tests for class Review """

    def __init__(self, *args, **kwargs):
        """ Inititialize models to test """

        super().__init__(*args, **kwargs)
        self.test_class = Review
        self.test_name = 'Review'
