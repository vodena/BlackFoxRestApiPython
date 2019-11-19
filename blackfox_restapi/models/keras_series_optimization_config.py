# coding: utf-8

"""
    BlackFox

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from blackfox_restapi.models.input_config import InputConfig  # noqa: F401,E501
from blackfox_restapi.models.input_window_range_config import InputWindowRangeConfig  # noqa: F401,E501
from blackfox_restapi.models.optimization_engine_config import OptimizationEngineConfig  # noqa: F401,E501
from blackfox_restapi.models.output_window_config import OutputWindowConfig  # noqa: F401,E501
from blackfox_restapi.models.range import Range  # noqa: F401,E501


class KerasSeriesOptimizationConfig(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'input_window_range_configs': 'list[InputWindowRangeConfig]',
        'output_window_configs': 'list[OutputWindowConfig]',
        'output_sample_step': 'int',
        'dropout': 'Range',
        'batch_size': 'int',
        'dataset_id': 'str',
        'inputs': 'list[InputConfig]',
        'output_ranges': 'list[Range]',
        'problem_type': 'str',
        'hidden_layer_count_range': 'Range',
        'neurons_per_layer': 'Range',
        'training_algorithms': 'list[str]',
        'activation_functions': 'list[str]',
        'max_epoch': 'int',
        'cross_validation': 'bool',
        'validation_split': 'float',
        'random_seed': 'int',
        'engine_config': 'OptimizationEngineConfig'
    }

    attribute_map = {
        'input_window_range_configs': 'inputWindowRangeConfigs',
        'output_window_configs': 'outputWindowConfigs',
        'output_sample_step': 'outputSampleStep',
        'dropout': 'dropout',
        'batch_size': 'batchSize',
        'dataset_id': 'datasetId',
        'inputs': 'inputs',
        'output_ranges': 'outputRanges',
        'problem_type': 'problemType',
        'hidden_layer_count_range': 'hiddenLayerCountRange',
        'neurons_per_layer': 'neuronsPerLayer',
        'training_algorithms': 'trainingAlgorithms',
        'activation_functions': 'activationFunctions',
        'max_epoch': 'maxEpoch',
        'cross_validation': 'crossValidation',
        'validation_split': 'validationSplit',
        'random_seed': 'randomSeed',
        'engine_config': 'engineConfig'
    }

    def __init__(self,
    input_window_range_configs=None,
    output_window_configs=None,
    output_sample_step=1,
    dropout=None,
    batch_size=32,
    dataset_id=None,
    inputs=None,
    output_ranges=None,
    problem_type='Regression',
    hidden_layer_count_range=None,
    neurons_per_layer=None,
    training_algorithms=["SGD", "RMSprop", "Adagrad", "Adadelta", "Adam", "Adamax", "Nadam"],
    activation_functions=["SoftMax", "Elu", "Selu", "SoftPlus",
                                      "SoftSign", "ReLu", "TanH", "Sigmoid",
                                      "HardSigmoid", "Linear"],
    max_epoch=3000,
    cross_validation=False,
    validation_split=0.2,
    random_seed=300,
    engine_config=OptimizationEngineConfig()
    ):  # noqa: E501
        """KerasSeriesOptimizationConfig - a model defined in Swagger"""  # noqa: E501

        self._input_window_range_configs = None
        self._output_window_configs = None
        self._output_sample_step = None
        self._dropout = None
        self._batch_size = None
        self._dataset_id = None
        self._inputs = None
        self._output_ranges = None
        self._problem_type = None
        self._hidden_layer_count_range = None
        self._neurons_per_layer = None
        self._training_algorithms = None
        self._activation_functions = None
        self._max_epoch = None
        self._cross_validation = None
        self._validation_split = None
        self._random_seed = None
        self._engine_config = None
        self.discriminator = None

        if input_window_range_configs is not None:
            self.input_window_range_configs = input_window_range_configs
        if output_window_configs is not None:
            self.output_window_configs = output_window_configs
        if output_sample_step is not None:
            self.output_sample_step = output_sample_step
        if dropout is not None:
            self.dropout = dropout
        if batch_size is not None:
            self.batch_size = batch_size
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if inputs is not None:
            self.inputs = inputs
        if output_ranges is not None:
            self.output_ranges = output_ranges
        if problem_type is not None:
            self.problem_type = problem_type
        if hidden_layer_count_range is not None:
            self.hidden_layer_count_range = hidden_layer_count_range
        if neurons_per_layer is not None:
            self.neurons_per_layer = neurons_per_layer
        if training_algorithms is not None:
            self.training_algorithms = training_algorithms
        if activation_functions is not None:
            self.activation_functions = activation_functions
        self.max_epoch = max_epoch
        if cross_validation is not None:
            self.cross_validation = cross_validation
        self.validation_split = validation_split
        if random_seed is not None:
            self.random_seed = random_seed
        if engine_config is not None:
            self.engine_config = engine_config

    @property
    def input_window_range_configs(self):
        """Gets the input_window_range_configs of this KerasSeriesOptimizationConfig.  # noqa: E501


        :return: The input_window_range_configs of this KerasSeriesOptimizationConfig.  # noqa: E501
        :rtype: list[InputWindowRangeConfig]
        """
        return self._input_window_range_configs

    @input_window_range_configs.setter
    def input_window_range_configs(self, input_window_range_configs):
        """Sets the input_window_range_configs of this KerasSeriesOptimizationConfig.


        :param input_window_range_configs: The input_window_range_configs of this KerasSeriesOptimizationConfig.  # noqa: E501
        :type: list[InputWindowRangeConfig]
        """

        self._input_window_range_configs = input_window_range_configs

    @property
    def output_window_configs(self):
        """Gets the output_window_configs of this KerasSeriesOptimizationConfig.  # noqa: E501


        :return: The output_window_configs of this KerasSeriesOptimizationConfig.  # noqa: E501
        :rtype: list[OutputWindowConfig]
        """
        return self._output_window_configs

    @output_window_configs.setter
    def output_window_configs(self, output_window_configs):
        """Sets the output_window_configs of this KerasSeriesOptimizationConfig.


        :param output_window_configs: The output_window_configs of this KerasSeriesOptimizationConfig.  # noqa: E501
        :type: list[OutputWindowConfig]
        """

        self._output_window_configs = output_window_configs

    @property
    def output_sample_step(self):
        """Gets the output_sample_step of this KerasSeriesOptimizationConfig.  # noqa: E501


        :return: The output_sample_step of this KerasSeriesOptimizationConfig.  # noqa: E501
        :rtype: int
        """
        return self._output_sample_step

    @output_sample_step.setter
    def output_sample_step(self, output_sample_step):
        """Sets the output_sample_step of this KerasSeriesOptimizationConfig.


        :param output_sample_step: The output_sample_step of this KerasSeriesOptimizationConfig.  # noqa: E501
        :type: int
        """

        self._output_sample_step = output_sample_step

    @property
    def dropout(self):
        """Gets the dropout of this KerasSeriesOptimizationConfig.  # noqa: E501


        :return: The dropout of this KerasSeriesOptimizationConfig.  # noqa: E501
        :rtype: Range
        """
        return self._dropout

    @dropout.setter
    def dropout(self, dropout):
        """Sets the dropout of this KerasSeriesOptimizationConfig.


        :param dropout: The dropout of this KerasSeriesOptimizationConfig.  # noqa: E501
        :type: Range
        """

        self._dropout = dropout

    @property
    def batch_size(self):
        """Gets the batch_size of this KerasSeriesOptimizationConfig.  # noqa: E501


        :return: The batch_size of this KerasSeriesOptimizationConfig.  # noqa: E501
        :rtype: int
        """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        """Sets the batch_size of this KerasSeriesOptimizationConfig.


        :param batch_size: The batch_size of this KerasSeriesOptimizationConfig.  # noqa: E501
        :type: int
        """

        self._batch_size = batch_size

    @property
    def dataset_id(self):
        """Gets the dataset_id of this KerasSeriesOptimizationConfig.  # noqa: E501

        Data set id on which to train network  # noqa: E501

        :return: The dataset_id of this KerasSeriesOptimizationConfig.  # noqa: E501
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this KerasSeriesOptimizationConfig.

        Data set id on which to train network  # noqa: E501

        :param dataset_id: The dataset_id of this KerasSeriesOptimizationConfig.  # noqa: E501
        :type: str
        """

        self._dataset_id = dataset_id

    @property
    def inputs(self):
        """Gets the inputs of this KerasSeriesOptimizationConfig.  # noqa: E501

        Define min and max value for each output column(feature), and is input optional  # noqa: E501

        :return: The inputs of this KerasSeriesOptimizationConfig.  # noqa: E501
        :rtype: list[InputConfig]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this KerasSeriesOptimizationConfig.

        Define min and max value for each output column(feature), and is input optional  # noqa: E501

        :param inputs: The inputs of this KerasSeriesOptimizationConfig.  # noqa: E501
        :type: list[InputConfig]
        """

        self._inputs = inputs

    @property
    def output_ranges(self):
        """Gets the output_ranges of this KerasSeriesOptimizationConfig.  # noqa: E501

        Define min and max value for each output column(feature)  # noqa: E501

        :return: The output_ranges of this KerasSeriesOptimizationConfig.  # noqa: E501
        :rtype: list[Range]
        """
        return self._output_ranges

    @output_ranges.setter
    def output_ranges(self, output_ranges):
        """Sets the output_ranges of this KerasSeriesOptimizationConfig.

        Define min and max value for each output column(feature)  # noqa: E501

        :param output_ranges: The output_ranges of this KerasSeriesOptimizationConfig.  # noqa: E501
        :type: list[Range]
        """

        self._output_ranges = output_ranges

    @property
    def problem_type(self):
        """Gets the problem_type of this KerasSeriesOptimizationConfig.  # noqa: E501

        Defines the problem type. In case of binary classification,  there must be only one output column.  # noqa: E501

        :return: The problem_type of this KerasSeriesOptimizationConfig.  # noqa: E501
        :rtype: str
        """
        return self._problem_type

    @problem_type.setter
    def problem_type(self, problem_type):
        """Sets the problem_type of this KerasSeriesOptimizationConfig.

        Defines the problem type. In case of binary classification,  there must be only one output column.  # noqa: E501

        :param problem_type: The problem_type of this KerasSeriesOptimizationConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["Regression", "BinaryClassification", "MultiClassClassification"]  # noqa: E501
        if problem_type not in allowed_values:
            raise ValueError(
                "Invalid value for `problem_type` ({0}), must be one of {1}"  # noqa: E501
                .format(problem_type, allowed_values)
            )

        self._problem_type = problem_type

    @property
    def hidden_layer_count_range(self):
        """Gets the hidden_layer_count_range of this KerasSeriesOptimizationConfig.  # noqa: E501

        Range in which to search number of hidden layers  # noqa: E501

        :return: The hidden_layer_count_range of this KerasSeriesOptimizationConfig.  # noqa: E501
        :rtype: Range
        """
        return self._hidden_layer_count_range

    @hidden_layer_count_range.setter
    def hidden_layer_count_range(self, hidden_layer_count_range):
        """Sets the hidden_layer_count_range of this KerasSeriesOptimizationConfig.

        Range in which to search number of hidden layers  # noqa: E501

        :param hidden_layer_count_range: The hidden_layer_count_range of this KerasSeriesOptimizationConfig.  # noqa: E501
        :type: Range
        """

        self._hidden_layer_count_range = hidden_layer_count_range

    @property
    def neurons_per_layer(self):
        """Gets the neurons_per_layer of this KerasSeriesOptimizationConfig.  # noqa: E501

        Range in which to search number of neurons per layer  # noqa: E501

        :return: The neurons_per_layer of this KerasSeriesOptimizationConfig.  # noqa: E501
        :rtype: Range
        """
        return self._neurons_per_layer

    @neurons_per_layer.setter
    def neurons_per_layer(self, neurons_per_layer):
        """Sets the neurons_per_layer of this KerasSeriesOptimizationConfig.

        Range in which to search number of neurons per layer  # noqa: E501

        :param neurons_per_layer: The neurons_per_layer of this KerasSeriesOptimizationConfig.  # noqa: E501
        :type: Range
        """

        self._neurons_per_layer = neurons_per_layer

    @property
    def training_algorithms(self):
        """Gets the training_algorithms of this KerasSeriesOptimizationConfig.  # noqa: E501

        List of training algorithms to use  # noqa: E501

        :return: The training_algorithms of this KerasSeriesOptimizationConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._training_algorithms

    @training_algorithms.setter
    def training_algorithms(self, training_algorithms):
        """Sets the training_algorithms of this KerasSeriesOptimizationConfig.

        List of training algorithms to use  # noqa: E501

        :param training_algorithms: The training_algorithms of this KerasSeriesOptimizationConfig.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["SGD", "RMSprop", "Adagrad", "Adadelta", "Adam", "Adamax", "Nadam"]  # noqa: E501
        if not set(training_algorithms).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `training_algorithms` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(training_algorithms) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._training_algorithms = training_algorithms

    @property
    def activation_functions(self):
        """Gets the activation_functions of this KerasSeriesOptimizationConfig.  # noqa: E501

        List of activation functions to use  # noqa: E501

        :return: The activation_functions of this KerasSeriesOptimizationConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._activation_functions

    @activation_functions.setter
    def activation_functions(self, activation_functions):
        """Sets the activation_functions of this KerasSeriesOptimizationConfig.

        List of activation functions to use  # noqa: E501

        :param activation_functions: The activation_functions of this KerasSeriesOptimizationConfig.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["SoftMax", "Elu", "Selu", "SoftPlus", "SoftSign", "ReLu", "TanH", "Sigmoid", "HardSigmoid", "Linear"]  # noqa: E501
        if not set(activation_functions).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `activation_functions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(activation_functions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._activation_functions = activation_functions

    @property
    def max_epoch(self):
        """Gets the max_epoch of this KerasSeriesOptimizationConfig.  # noqa: E501

        Maximum number of epoch  # noqa: E501

        :return: The max_epoch of this KerasSeriesOptimizationConfig.  # noqa: E501
        :rtype: int
        """
        return self._max_epoch

    @max_epoch.setter
    def max_epoch(self, max_epoch):
        """Sets the max_epoch of this KerasSeriesOptimizationConfig.

        Maximum number of epoch  # noqa: E501

        :param max_epoch: The max_epoch of this KerasSeriesOptimizationConfig.  # noqa: E501
        :type: int
        """
        if max_epoch is None:
            raise ValueError("Invalid value for `max_epoch`, must not be `None`")  # noqa: E501
        if max_epoch is not None and max_epoch > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `max_epoch`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if max_epoch is not None and max_epoch < 1:  # noqa: E501
            raise ValueError("Invalid value for `max_epoch`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_epoch = max_epoch

    @property
    def cross_validation(self):
        """Gets the cross_validation of this KerasSeriesOptimizationConfig.  # noqa: E501

        Use cross validation  # noqa: E501

        :return: The cross_validation of this KerasSeriesOptimizationConfig.  # noqa: E501
        :rtype: bool
        """
        return self._cross_validation

    @cross_validation.setter
    def cross_validation(self, cross_validation):
        """Sets the cross_validation of this KerasSeriesOptimizationConfig.

        Use cross validation  # noqa: E501

        :param cross_validation: The cross_validation of this KerasSeriesOptimizationConfig.  # noqa: E501
        :type: bool
        """

        self._cross_validation = cross_validation

    @property
    def validation_split(self):
        """Gets the validation_split of this KerasSeriesOptimizationConfig.  # noqa: E501

        Portion of data set to use for validation, must be between 0 and 1.   Used only when CrossValidation = false.  # noqa: E501

        :return: The validation_split of this KerasSeriesOptimizationConfig.  # noqa: E501
        :rtype: float
        """
        return self._validation_split

    @validation_split.setter
    def validation_split(self, validation_split):
        """Sets the validation_split of this KerasSeriesOptimizationConfig.

        Portion of data set to use for validation, must be between 0 and 1.   Used only when CrossValidation = false.  # noqa: E501

        :param validation_split: The validation_split of this KerasSeriesOptimizationConfig.  # noqa: E501
        :type: float
        """
        if validation_split is None:
            raise ValueError("Invalid value for `validation_split`, must not be `None`")  # noqa: E501
        if validation_split is not None and validation_split > 1.0:  # noqa: E501
            raise ValueError("Invalid value for `validation_split`, must be a value less than or equal to `1.0`")  # noqa: E501
        if validation_split is not None and validation_split < 0.0:  # noqa: E501
            raise ValueError("Invalid value for `validation_split`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._validation_split = validation_split

    @property
    def random_seed(self):
        """Gets the random_seed of this KerasSeriesOptimizationConfig.  # noqa: E501

        Random number generator seed, if the value is zero, the rows will not be randomly shuffled  Used only if CrossValidation = false  # noqa: E501

        :return: The random_seed of this KerasSeriesOptimizationConfig.  # noqa: E501
        :rtype: int
        """
        return self._random_seed

    @random_seed.setter
    def random_seed(self, random_seed):
        """Sets the random_seed of this KerasSeriesOptimizationConfig.

        Random number generator seed, if the value is zero, the rows will not be randomly shuffled  Used only if CrossValidation = false  # noqa: E501

        :param random_seed: The random_seed of this KerasSeriesOptimizationConfig.  # noqa: E501
        :type: int
        """

        self._random_seed = random_seed

    @property
    def engine_config(self):
        """Gets the engine_config of this KerasSeriesOptimizationConfig.  # noqa: E501

        Optimization engine config  # noqa: E501

        :return: The engine_config of this KerasSeriesOptimizationConfig.  # noqa: E501
        :rtype: OptimizationEngineConfig
        """
        return self._engine_config

    @engine_config.setter
    def engine_config(self, engine_config):
        """Sets the engine_config of this KerasSeriesOptimizationConfig.

        Optimization engine config  # noqa: E501

        :param engine_config: The engine_config of this KerasSeriesOptimizationConfig.  # noqa: E501
        :type: OptimizationEngineConfig
        """

        self._engine_config = engine_config

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(KerasSeriesOptimizationConfig, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KerasSeriesOptimizationConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
