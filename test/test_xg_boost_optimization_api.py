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
from blackfox_restapi.api.xg_boost_optimization_api import XGBoostOptimizationApi  # noqa: E501
from blackfox_restapi.rest import ApiException


class TestXGBoostOptimizationApi(unittest.TestCase):
    """XGBoostOptimizationApi unit test stubs"""

    def setUp(self):
        self.api = blackfox_restapi.api.xg_boost_optimization_api.XGBoostOptimizationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete(self):
        """Test case for delete

        Delete optimization from optimization service  # noqa: E501
        """
        pass

    def test_get_model_id(self):
        """Test case for get_model_id

        Get id of best model for given generation  # noqa: E501
        """
        pass

    def test_get_status(self):
        """Test case for get_status

        Get status of optimization  # noqa: E501
        """
        pass

    def test_start(self):
        """Test case for start

        Start XGBoost optimization  # noqa: E501
        """
        pass

    def test_start_series(self):
        """Test case for start_series

        Starts new series optimization using XGBoost model  # noqa: E501
        """
        pass

    def test_stop(self):
        """Test case for stop

        Stop running optimization  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()