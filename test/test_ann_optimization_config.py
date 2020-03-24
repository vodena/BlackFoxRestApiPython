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
from blackfox_restapi.models.ann_optimization_config import AnnOptimizationConfig  # noqa: E501
from blackfox_restapi.rest import ApiException

class TestAnnOptimizationConfig(unittest.TestCase):
    """AnnOptimizationConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AnnOptimizationConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = blackfox_restapi.models.ann_optimization_config.AnnOptimizationConfig()  # noqa: E501
        if include_optional :
            return AnnOptimizationConfig(
                dropout = null, 
                batch_size = 56, 
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
                problem_type = Regression, 
                binary_optimization_metric = Auc, 
                hidden_layer_count_range = {"min":1,"max":15}, 
                neurons_per_layer = {"min":1,"max":10}, 
                training_algorithms = ["Adadelta","Adagrad","Adam","Adamax","Nadam","RMSprop","SGD"], 
                activation_functions = ["Elu","HardSigmoid","Linear","ReLu","Selu","Sigmoid","SoftMax","SoftPlus","SoftSign","TanH"], 
                max_epoch = 1, 
                cross_validation = True, 
                validation_split = 0, 
                random_seed = 56, 
                engine_config = null
            )
        else :
            return AnnOptimizationConfig(
                max_epoch = 1,
                validation_split = 0,
        )

    def testAnnOptimizationConfig(self):
        """Test AnnOptimizationConfig"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()