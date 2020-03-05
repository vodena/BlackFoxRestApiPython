# coding: utf-8

"""
    BlackFox

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import blackfox_restapi
from blackfox_restapi.api.rnn_model_api import RnnModelApi  # noqa: E501
from blackfox_restapi.rest import ApiException


class TestRnnModelApi(unittest.TestCase):
    """RnnModelApi unit test stubs"""

    def setUp(self):
        self.api = blackfox_restapi.api.rnn_model_api.RnnModelApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_download(self):
        """Test case for download

        Download model file  # noqa: E501
        """
        pass

    def test_exists(self):
        """Test case for exists

        Check if model file exist  # noqa: E501
        """
        pass

    def test_get_metadata(self):
        """Test case for get_metadata

        Get model metadata  # noqa: E501
        """
        pass

    def test_upload(self):
        """Test case for upload

        Upload model file  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
