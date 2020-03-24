# coding: utf-8

"""
    BlackFox

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import blackfox_restapi
from blackfox_restapi.models.xg_boost_model import XGBoostModel  # noqa: E501
from blackfox_restapi.rest import ApiException

class TestXGBoostModel(unittest.TestCase):
    """XGBoostModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XGBoostModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = blackfox_restapi.models.xg_boost_model.XGBoostModel()  # noqa: E501
        if include_optional :
            return XGBoostModel(
                max_depth = 56, 
                min_child_weight = 56, 
                gamma = 1.337, 
                subsample = 1.337, 
                colsample_bytree = 1.337, 
                reg_alpha = 1.337, 
                learning_rate = 1.337, 
                feature_selection = [
                    True
                    ]
            )
        else :
            return XGBoostModel(
        )

    def testXGBoostModel(self):
        """Test XGBoostModel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
