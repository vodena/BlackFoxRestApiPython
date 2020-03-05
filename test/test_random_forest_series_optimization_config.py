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
from blackfox_restapi.models.random_forest_series_optimization_config import RandomForestSeriesOptimizationConfig  # noqa: E501
from blackfox_restapi.rest import ApiException

class TestRandomForestSeriesOptimizationConfig(unittest.TestCase):
    """RandomForestSeriesOptimizationConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RandomForestSeriesOptimizationConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = blackfox_restapi.models.random_forest_series_optimization_config.RandomForestSeriesOptimizationConfig()  # noqa: E501
        if include_optional :
            return RandomForestSeriesOptimizationConfig(
                input_window_range_configs = [
                    blackfox_restapi.models.input_window_range_config.InputWindowRangeConfig(
                        window = null, 
                        shift = null, 
                        step = null, 
                        aggregation_types = [
                            'Avg'
                            ], )
                    ], 
                output_window_configs = [
                    blackfox_restapi.models.output_window_config.OutputWindowConfig(
                        window = 56, 
                        shift = 56, )
                    ], 
                output_sample_step = 56, 
                dataset_id = '0', 
                inputs = [
                    blackfox_restapi.models.input_config.InputConfig(
                        range = null, 
                        is_optional = True, )
                    ], 
                output_ranges = [
                    blackfox_restapi.models.range.Range(
                        min = 1.337, 
                        max = 1.337, )
                    ], 
                problem_type = null, 
                validation_split = 0, 
                random_seed = 56, 
                engine_config = null, 
                number_of_estimators = null, 
                max_depth = null, 
                max_features = null
            )
        else :
            return RandomForestSeriesOptimizationConfig(
                validation_split = 0,
                number_of_estimators = null,
                max_depth = null,
                max_features = null,
        )

    def testRandomForestSeriesOptimizationConfig(self):
        """Test RandomForestSeriesOptimizationConfig"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()