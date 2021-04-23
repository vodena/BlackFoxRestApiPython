# coding: utf-8

"""
    BlackFox

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from blackfox_restapi.configuration import Configuration
from blackfox_restapi.models.optimization_engine_config import OptimizationEngineConfig
from blackfox_restapi.models.problem_type import ProblemType
from blackfox_restapi.models.binary_metric import BinaryMetric
from blackfox_restapi.models.regression_metric import RegressionMetric

class XGBoostOptimizationConfig(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'dataset_id': 'str',
        'validation_set_id': 'str',
        'inputs': 'list[InputConfig]',
        'outputs': 'list[OutputConfig]',
        'validation_split': 'float',
        'random_seed': 'int',
        'problem_type': 'ProblemType',
        'binary_optimization_metric': 'BinaryMetric',
        'regression_optimization_metric': 'RegressionMetric',
        'n_estimators': 'RangeInt',
        'max_depth': 'RangeInt',
        'min_child_weight': 'RangeInt',
        'gamma': 'Range',
        'subsample': 'Range',
        'colsample_bytree': 'Range',
        'reg_alpha': 'Range',
        'learning_rate': 'Range',
        'engine_config': 'OptimizationEngineConfig'
    }

    attribute_map = {
        'dataset_id': 'datasetId',
        'validation_set_id': 'validationSetId',
        'inputs': 'inputs',
        'outputs': 'outputs',
        'validation_split': 'validationSplit',
        'random_seed': 'randomSeed',
        'problem_type': 'problemType',
        'binary_optimization_metric': 'binaryOptimizationMetric',
        'regression_optimization_metric': 'regressionOptimizationMetric',
        'n_estimators': 'nEstimators',
        'max_depth': 'maxDepth',
        'min_child_weight': 'minChildWeight',
        'gamma': 'gamma',
        'subsample': 'subsample',
        'colsample_bytree': 'colsampleBytree',
        'reg_alpha': 'regAlpha',
        'learning_rate': 'learningRate',
        'engine_config': 'engineConfig'
    }

    def __init__(self, dataset_id=None, validation_set_id=None, inputs=None, outputs=None, validation_split=0.2, random_seed=300, problem_type=ProblemType.REGRESSION, binary_optimization_metric=BinaryMetric.ROC_AUC, regression_optimization_metric=RegressionMetric.MAE, n_estimators=None, max_depth=None, min_child_weight=None, gamma=None, subsample=None, colsample_bytree=None, reg_alpha=None, learning_rate=None, engine_config=OptimizationEngineConfig(), local_vars_configuration=None):  # noqa: E501
        """XGBoostOptimizationConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dataset_id = None
        self._validation_set_id = None
        self._inputs = None
        self._outputs = None
        self._validation_split = None
        self._random_seed = None
        self._problem_type = None
        self._binary_optimization_metric = None
        self._regression_optimization_metric = None
        self._n_estimators = None
        self._max_depth = None
        self._min_child_weight = None
        self._gamma = None
        self._subsample = None
        self._colsample_bytree = None
        self._reg_alpha = None
        self._learning_rate = None
        self._engine_config = None
        self.discriminator = None

        self.dataset_id = dataset_id
        self.validation_set_id = validation_set_id
        self.inputs = inputs
        self.outputs = outputs
        if validation_split is not None:
            self.validation_split = validation_split
        self.random_seed = random_seed
        if problem_type is not None:
            self.problem_type = problem_type
        if binary_optimization_metric is not None:
            self.binary_optimization_metric = binary_optimization_metric
        if regression_optimization_metric is not None:
            self.regression_optimization_metric = regression_optimization_metric
        if n_estimators is not None:
            self.n_estimators = n_estimators
        if max_depth is not None:
            self.max_depth = max_depth
        if min_child_weight is not None:
            self.min_child_weight = min_child_weight
        if gamma is not None:
            self.gamma = gamma
        if subsample is not None:
            self.subsample = subsample
        if colsample_bytree is not None:
            self.colsample_bytree = colsample_bytree
        if reg_alpha is not None:
            self.reg_alpha = reg_alpha
        if learning_rate is not None:
            self.learning_rate = learning_rate
        self.engine_config = engine_config

    @property
    def dataset_id(self):
        """Gets the dataset_id of this XGBoostOptimizationConfig.  # noqa: E501


        :return: The dataset_id of this XGBoostOptimizationConfig.  # noqa: E501
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this XGBoostOptimizationConfig.


        :param dataset_id: The dataset_id of this XGBoostOptimizationConfig.  # noqa: E501
        :type: str
        """

        self._dataset_id = dataset_id

    @property
    def validation_set_id(self):
        """Gets the validation_set_id of this XGBoostOptimizationConfig.  # noqa: E501


        :return: The validation_set_id of this XGBoostOptimizationConfig.  # noqa: E501
        :rtype: str
        """
        return self._validation_set_id

    @validation_set_id.setter
    def validation_set_id(self, validation_set_id):
        """Sets the validation_set_id of this XGBoostOptimizationConfig.


        :param validation_set_id: The validation_set_id of this XGBoostOptimizationConfig.  # noqa: E501
        :type: str
        """

        self._validation_set_id = validation_set_id

    @property
    def inputs(self):
        """Gets the inputs of this XGBoostOptimizationConfig.  # noqa: E501


        :return: The inputs of this XGBoostOptimizationConfig.  # noqa: E501
        :rtype: list[InputConfig]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this XGBoostOptimizationConfig.


        :param inputs: The inputs of this XGBoostOptimizationConfig.  # noqa: E501
        :type: list[InputConfig]
        """

        self._inputs = inputs

    @property
    def outputs(self):
        """Gets the outputs of this XGBoostOptimizationConfig.  # noqa: E501


        :return: The outputs of this XGBoostOptimizationConfig.  # noqa: E501
        :rtype: list[OutputConfig]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this XGBoostOptimizationConfig.


        :param outputs: The outputs of this XGBoostOptimizationConfig.  # noqa: E501
        :type: list[OutputConfig]
        """

        self._outputs = outputs

    @property
    def validation_split(self):
        """Gets the validation_split of this XGBoostOptimizationConfig.  # noqa: E501


        :return: The validation_split of this XGBoostOptimizationConfig.  # noqa: E501
        :rtype: float
        """
        return self._validation_split

    @validation_split.setter
    def validation_split(self, validation_split):
        """Sets the validation_split of this XGBoostOptimizationConfig.


        :param validation_split: The validation_split of this XGBoostOptimizationConfig.  # noqa: E501
        :type: float
        """

        self._validation_split = validation_split

    @property
    def random_seed(self):
        """Gets the random_seed of this XGBoostOptimizationConfig.  # noqa: E501


        :return: The random_seed of this XGBoostOptimizationConfig.  # noqa: E501
        :rtype: int
        """
        return self._random_seed

    @random_seed.setter
    def random_seed(self, random_seed):
        """Sets the random_seed of this XGBoostOptimizationConfig.


        :param random_seed: The random_seed of this XGBoostOptimizationConfig.  # noqa: E501
        :type: int
        """

        self._random_seed = random_seed

    @property
    def problem_type(self):
        """Gets the problem_type of this XGBoostOptimizationConfig.  # noqa: E501

        Defines the problem type. In case of binary classification,  there must be only one output column.  # noqa: E501

        :return: The problem_type of this XGBoostOptimizationConfig.  # noqa: E501
        :rtype: ProblemType
        """
        return self._problem_type

    @problem_type.setter
    def problem_type(self, problem_type):
        """Sets the problem_type of this XGBoostOptimizationConfig.

        Defines the problem type. In case of binary classification,  there must be only one output column.  # noqa: E501

        :param problem_type: The problem_type of this XGBoostOptimizationConfig.  # noqa: E501
        :type: ProblemType
        """

        self._problem_type = problem_type

    @property
    def binary_optimization_metric(self):
        """Gets the binary_optimization_metric of this XGBoostOptimizationConfig.  # noqa: E501

        USED ONLY IN BINARY CLASSIFICATION.  Default metric: ROC_AUC (Area under ROC curve).   Depending on the task at hand, it is recommended to choose an appropriate metric to optimize.  # noqa: E501

        :return: The binary_optimization_metric of this XGBoostOptimizationConfig.  # noqa: E501
        :rtype: BinaryMetric
        """
        return self._binary_optimization_metric

    @binary_optimization_metric.setter
    def binary_optimization_metric(self, binary_optimization_metric):
        """Sets the binary_optimization_metric of this XGBoostOptimizationConfig.

        USED ONLY IN BINARY CLASSIFICATION.  Default metric: ROC_AUC (Area under ROC curve).   Depending on the task at hand, it is recommended to choose an appropriate metric to optimize.  # noqa: E501

        :param binary_optimization_metric: The binary_optimization_metric of this XGBoostOptimizationConfig.  # noqa: E501
        :type: BinaryMetric
        """

        self._binary_optimization_metric = binary_optimization_metric

    @property
    def regression_optimization_metric(self):
        """Gets the regression_optimization_metric of this XGBoostOptimizationConfig.  # noqa: E501

        USED ONLY IN REGRESSION.  Default metric: MAE (MEAN ABSOLUTE ERROR).   Depending on the task at hand, it is recommended to choose an appropriate metric to optimize.  # noqa: E501

        :return: The regression_optimization_metric of this XGBoostOptimizationConfig.  # noqa: E501
        :rtype: RegressionMetric
        """
        return self._regression_optimization_metric

    @regression_optimization_metric.setter
    def regression_optimization_metric(self, regression_optimization_metric):
        """Sets the regression_optimization_metric of this XGBoostOptimizationConfig.

        USED ONLY IN REGRESSION.  Default metric: MAE (MEAN ABSOLUTE ERROR).   Depending on the task at hand, it is recommended to choose an appropriate metric to optimize.  # noqa: E501

        :param regression_optimization_metric: The regression_optimization_metric of this XGBoostOptimizationConfig.  # noqa: E501
        :type: RegressionMetric
        """

        self._regression_optimization_metric = regression_optimization_metric

    @property
    def n_estimators(self):
        """Gets the n_estimators of this XGBoostOptimizationConfig.  # noqa: E501

        N Estimators  # noqa: E501

        :return: The n_estimators of this XGBoostOptimizationConfig.  # noqa: E501
        :rtype: RangeInt
        """
        return self._n_estimators

    @n_estimators.setter
    def n_estimators(self, n_estimators):
        """Sets the n_estimators of this XGBoostOptimizationConfig.

        N Estimators  # noqa: E501

        :param n_estimators: The n_estimators of this XGBoostOptimizationConfig.  # noqa: E501
        :type: RangeInt
        """
        if self.local_vars_configuration.client_side_validation and n_estimators is None:  # noqa: E501
            raise ValueError("Invalid value for `n_estimators`, must not be `None`")  # noqa: E501

        self._n_estimators = n_estimators

    @property
    def max_depth(self):
        """Gets the max_depth of this XGBoostOptimizationConfig.  # noqa: E501

        MaxDepth  # noqa: E501

        :return: The max_depth of this XGBoostOptimizationConfig.  # noqa: E501
        :rtype: RangeInt
        """
        return self._max_depth

    @max_depth.setter
    def max_depth(self, max_depth):
        """Sets the max_depth of this XGBoostOptimizationConfig.

        MaxDepth  # noqa: E501

        :param max_depth: The max_depth of this XGBoostOptimizationConfig.  # noqa: E501
        :type: RangeInt
        """
        if self.local_vars_configuration.client_side_validation and max_depth is None:  # noqa: E501
            raise ValueError("Invalid value for `max_depth`, must not be `None`")  # noqa: E501

        self._max_depth = max_depth

    @property
    def min_child_weight(self):
        """Gets the min_child_weight of this XGBoostOptimizationConfig.  # noqa: E501

        MinChildWeight  # noqa: E501

        :return: The min_child_weight of this XGBoostOptimizationConfig.  # noqa: E501
        :rtype: RangeInt
        """
        return self._min_child_weight

    @min_child_weight.setter
    def min_child_weight(self, min_child_weight):
        """Sets the min_child_weight of this XGBoostOptimizationConfig.

        MinChildWeight  # noqa: E501

        :param min_child_weight: The min_child_weight of this XGBoostOptimizationConfig.  # noqa: E501
        :type: RangeInt
        """
        if self.local_vars_configuration.client_side_validation and min_child_weight is None:  # noqa: E501
            raise ValueError("Invalid value for `min_child_weight`, must not be `None`")  # noqa: E501

        self._min_child_weight = min_child_weight

    @property
    def gamma(self):
        """Gets the gamma of this XGBoostOptimizationConfig.  # noqa: E501

        Gamma  # noqa: E501

        :return: The gamma of this XGBoostOptimizationConfig.  # noqa: E501
        :rtype: Range
        """
        return self._gamma

    @gamma.setter
    def gamma(self, gamma):
        """Sets the gamma of this XGBoostOptimizationConfig.

        Gamma  # noqa: E501

        :param gamma: The gamma of this XGBoostOptimizationConfig.  # noqa: E501
        :type: Range
        """
        if self.local_vars_configuration.client_side_validation and gamma is None:  # noqa: E501
            raise ValueError("Invalid value for `gamma`, must not be `None`")  # noqa: E501

        self._gamma = gamma

    @property
    def subsample(self):
        """Gets the subsample of this XGBoostOptimizationConfig.  # noqa: E501

        Subsample  # noqa: E501

        :return: The subsample of this XGBoostOptimizationConfig.  # noqa: E501
        :rtype: Range
        """
        return self._subsample

    @subsample.setter
    def subsample(self, subsample):
        """Sets the subsample of this XGBoostOptimizationConfig.

        Subsample  # noqa: E501

        :param subsample: The subsample of this XGBoostOptimizationConfig.  # noqa: E501
        :type: Range
        """
        if self.local_vars_configuration.client_side_validation and subsample is None:  # noqa: E501
            raise ValueError("Invalid value for `subsample`, must not be `None`")  # noqa: E501

        self._subsample = subsample

    @property
    def colsample_bytree(self):
        """Gets the colsample_bytree of this XGBoostOptimizationConfig.  # noqa: E501

        ColsampleBytree  # noqa: E501

        :return: The colsample_bytree of this XGBoostOptimizationConfig.  # noqa: E501
        :rtype: Range
        """
        return self._colsample_bytree

    @colsample_bytree.setter
    def colsample_bytree(self, colsample_bytree):
        """Sets the colsample_bytree of this XGBoostOptimizationConfig.

        ColsampleBytree  # noqa: E501

        :param colsample_bytree: The colsample_bytree of this XGBoostOptimizationConfig.  # noqa: E501
        :type: Range
        """
        if self.local_vars_configuration.client_side_validation and colsample_bytree is None:  # noqa: E501
            raise ValueError("Invalid value for `colsample_bytree`, must not be `None`")  # noqa: E501

        self._colsample_bytree = colsample_bytree

    @property
    def reg_alpha(self):
        """Gets the reg_alpha of this XGBoostOptimizationConfig.  # noqa: E501

        RegAlpha  # noqa: E501

        :return: The reg_alpha of this XGBoostOptimizationConfig.  # noqa: E501
        :rtype: Range
        """
        return self._reg_alpha

    @reg_alpha.setter
    def reg_alpha(self, reg_alpha):
        """Sets the reg_alpha of this XGBoostOptimizationConfig.

        RegAlpha  # noqa: E501

        :param reg_alpha: The reg_alpha of this XGBoostOptimizationConfig.  # noqa: E501
        :type: Range
        """
        if self.local_vars_configuration.client_side_validation and reg_alpha is None:  # noqa: E501
            raise ValueError("Invalid value for `reg_alpha`, must not be `None`")  # noqa: E501

        self._reg_alpha = reg_alpha

    @property
    def learning_rate(self):
        """Gets the learning_rate of this XGBoostOptimizationConfig.  # noqa: E501

        LearningRate  # noqa: E501

        :return: The learning_rate of this XGBoostOptimizationConfig.  # noqa: E501
        :rtype: Range
        """
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, learning_rate):
        """Sets the learning_rate of this XGBoostOptimizationConfig.

        LearningRate  # noqa: E501

        :param learning_rate: The learning_rate of this XGBoostOptimizationConfig.  # noqa: E501
        :type: Range
        """
        if self.local_vars_configuration.client_side_validation and learning_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `learning_rate`, must not be `None`")  # noqa: E501

        self._learning_rate = learning_rate

    @property
    def engine_config(self):
        """Gets the engine_config of this XGBoostOptimizationConfig.  # noqa: E501

        Optimization engine config  # noqa: E501

        :return: The engine_config of this XGBoostOptimizationConfig.  # noqa: E501
        :rtype: OptimizationEngineConfig
        """
        return self._engine_config

    @engine_config.setter
    def engine_config(self, engine_config):
        """Sets the engine_config of this XGBoostOptimizationConfig.

        Optimization engine config  # noqa: E501

        :param engine_config: The engine_config of this XGBoostOptimizationConfig.  # noqa: E501
        :type: OptimizationEngineConfig
        """

        self._engine_config = engine_config

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, XGBoostOptimizationConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XGBoostOptimizationConfig):
            return True

        return self.to_dict() != other.to_dict()
