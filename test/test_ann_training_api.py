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
from blackfox_restapi.api.ann_training_api import AnnTrainingApi  # noqa: E501
from blackfox_restapi.rest import ApiException


class TestAnnTrainingApi(unittest.TestCase):
    """AnnTrainingApi unit test stubs"""

    def setUp(self):
        self.api = blackfox_restapi.api.ann_training_api.AnnTrainingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_train(self):
        """Test case for train

        """
        pass

    def test_train_series(self):
        """Test case for train_series

        """
        pass


if __name__ == '__main__':
    unittest.main()
