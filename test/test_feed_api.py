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
from stylelens_sdk.apis.feed_api import FeedApi


class TestFeedApi(unittest.TestCase):
    """ FeedApi unit test stubs """

    def setUp(self):
        self.api = stylelens_sdk.apis.feed_api.FeedApi()

    def tearDown(self):
        pass

    def test_get_feeds(self):
        """
        Test case for get_feeds

        
        """
        pass


if __name__ == '__main__':
    unittest.main()