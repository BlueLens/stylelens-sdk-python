# coding: utf-8

"""
    style-api

    This is a API document for Stylens Service

    OpenAPI spec version: 0.0.1
    Contact: master@bluehack.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import stylelens_sdk
from stylelens_sdk.rest import ApiException
from stylelens_sdk.apis.object_api import ObjectApi


class TestObjectApi(unittest.TestCase):
    """ ObjectApi unit test stubs """

    def setUp(self):
        self.api = stylelens_sdk.apis.object_api.ObjectApi()

    def tearDown(self):
        pass

    def test_get_objects_by_image_file(self):
        """
        Test case for get_objects_by_image_file

        Query to search objects and products
        """
        pass

    def test_get_objects_by_product_id(self):
        """
        Test case for get_objects_by_product_id

        Query to search multiple objects
        """
        pass


if __name__ == '__main__':
    unittest.main()
