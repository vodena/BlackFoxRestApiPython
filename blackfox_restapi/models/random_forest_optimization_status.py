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


class RandomForestOptimizationStatus(object):
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
        'feature_selection': 'list[bool]',
        'guid': 'str',
        'state': 'OptimizationState',
        'generation': 'int',
        'total_generations': 'int',
        'validation_set_error': 'float',
        'training_set_error': 'float',
        'best_model': 'RandomForestModel',
        'start_date_time': 'datetime',
        'estimated_date_time': 'datetime',
        'generation_seconds': 'int',
        'metric_name': 'str'
    }

    attribute_map = {
        'feature_selection': 'featureSelection',
        'guid': 'guid',
        'state': 'state',
        'generation': 'generation',
        'total_generations': 'totalGenerations',
        'validation_set_error': 'validationSetError',
        'training_set_error': 'trainingSetError',
        'best_model': 'bestModel',
        'start_date_time': 'startDateTime',
        'estimated_date_time': 'estimatedDateTime',
        'generation_seconds': 'generationSeconds',
        'metric_name': 'metricName'
    }

    def __init__(self, feature_selection=None, guid=None, state=None, generation=None, total_generations=None, validation_set_error=None, training_set_error=None, best_model=None, start_date_time=None, estimated_date_time=None, generation_seconds=None, metric_name=None, local_vars_configuration=None):  # noqa: E501
        """RandomForestOptimizationStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._feature_selection = None
        self._guid = None
        self._state = None
        self._generation = None
        self._total_generations = None
        self._validation_set_error = None
        self._training_set_error = None
        self._best_model = None
        self._start_date_time = None
        self._estimated_date_time = None
        self._generation_seconds = None
        self._metric_name = None
        self.discriminator = None

        self.feature_selection = feature_selection
        if guid is not None:
            self.guid = guid
        if state is not None:
            self.state = state
        if generation is not None:
            self.generation = generation
        if total_generations is not None:
            self.total_generations = total_generations
        if validation_set_error is not None:
            self.validation_set_error = validation_set_error
        if training_set_error is not None:
            self.training_set_error = training_set_error
        self.best_model = best_model
        if start_date_time is not None:
            self.start_date_time = start_date_time
        if estimated_date_time is not None:
            self.estimated_date_time = estimated_date_time
        if generation_seconds is not None:
            self.generation_seconds = generation_seconds
        self.metric_name = metric_name

    @property
    def feature_selection(self):
        """Gets the feature_selection of this RandomForestOptimizationStatus.  # noqa: E501

        А bool value for each input indicating whether that input is significant  # noqa: E501

        :return: The feature_selection of this RandomForestOptimizationStatus.  # noqa: E501
        :rtype: list[bool]
        """
        return self._feature_selection

    @feature_selection.setter
    def feature_selection(self, feature_selection):
        """Sets the feature_selection of this RandomForestOptimizationStatus.

        А bool value for each input indicating whether that input is significant  # noqa: E501

        :param feature_selection: The feature_selection of this RandomForestOptimizationStatus.  # noqa: E501
        :type: list[bool]
        """

        self._feature_selection = feature_selection

    @property
    def guid(self):
        """Gets the guid of this RandomForestOptimizationStatus.  # noqa: E501

        Guid  # noqa: E501

        :return: The guid of this RandomForestOptimizationStatus.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this RandomForestOptimizationStatus.

        Guid  # noqa: E501

        :param guid: The guid of this RandomForestOptimizationStatus.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def state(self):
        """Gets the state of this RandomForestOptimizationStatus.  # noqa: E501

        Optimization state (Active, Finished, Stopped, Error)  # noqa: E501

        :return: The state of this RandomForestOptimizationStatus.  # noqa: E501
        :rtype: OptimizationState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this RandomForestOptimizationStatus.

        Optimization state (Active, Finished, Stopped, Error)  # noqa: E501

        :param state: The state of this RandomForestOptimizationStatus.  # noqa: E501
        :type: OptimizationState
        """

        self._state = state

    @property
    def generation(self):
        """Gets the generation of this RandomForestOptimizationStatus.  # noqa: E501

        Current generation  # noqa: E501

        :return: The generation of this RandomForestOptimizationStatus.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this RandomForestOptimizationStatus.

        Current generation  # noqa: E501

        :param generation: The generation of this RandomForestOptimizationStatus.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def total_generations(self):
        """Gets the total_generations of this RandomForestOptimizationStatus.  # noqa: E501

        Total number of generations  # noqa: E501

        :return: The total_generations of this RandomForestOptimizationStatus.  # noqa: E501
        :rtype: int
        """
        return self._total_generations

    @total_generations.setter
    def total_generations(self, total_generations):
        """Sets the total_generations of this RandomForestOptimizationStatus.

        Total number of generations  # noqa: E501

        :param total_generations: The total_generations of this RandomForestOptimizationStatus.  # noqa: E501
        :type: int
        """

        self._total_generations = total_generations

    @property
    def validation_set_error(self):
        """Gets the validation_set_error of this RandomForestOptimizationStatus.  # noqa: E501

        Error on validation set  # noqa: E501

        :return: The validation_set_error of this RandomForestOptimizationStatus.  # noqa: E501
        :rtype: float
        """
        return self._validation_set_error

    @validation_set_error.setter
    def validation_set_error(self, validation_set_error):
        """Sets the validation_set_error of this RandomForestOptimizationStatus.

        Error on validation set  # noqa: E501

        :param validation_set_error: The validation_set_error of this RandomForestOptimizationStatus.  # noqa: E501
        :type: float
        """

        self._validation_set_error = validation_set_error

    @property
    def training_set_error(self):
        """Gets the training_set_error of this RandomForestOptimizationStatus.  # noqa: E501

        Error on training set  # noqa: E501

        :return: The training_set_error of this RandomForestOptimizationStatus.  # noqa: E501
        :rtype: float
        """
        return self._training_set_error

    @training_set_error.setter
    def training_set_error(self, training_set_error):
        """Sets the training_set_error of this RandomForestOptimizationStatus.

        Error on training set  # noqa: E501

        :param training_set_error: The training_set_error of this RandomForestOptimizationStatus.  # noqa: E501
        :type: float
        """

        self._training_set_error = training_set_error

    @property
    def best_model(self):
        """Gets the best_model of this RandomForestOptimizationStatus.  # noqa: E501

        Best model, only set if optimization is finished  # noqa: E501

        :return: The best_model of this RandomForestOptimizationStatus.  # noqa: E501
        :rtype: RandomForestModel
        """
        return self._best_model

    @best_model.setter
    def best_model(self, best_model):
        """Sets the best_model of this RandomForestOptimizationStatus.

        Best model, only set if optimization is finished  # noqa: E501

        :param best_model: The best_model of this RandomForestOptimizationStatus.  # noqa: E501
        :type: RandomForestModel
        """

        self._best_model = best_model

    @property
    def start_date_time(self):
        """Gets the start_date_time of this RandomForestOptimizationStatus.  # noqa: E501

        Optimization start date and time  # noqa: E501

        :return: The start_date_time of this RandomForestOptimizationStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this RandomForestOptimizationStatus.

        Optimization start date and time  # noqa: E501

        :param start_date_time: The start_date_time of this RandomForestOptimizationStatus.  # noqa: E501
        :type: datetime
        """

        self._start_date_time = start_date_time

    @property
    def estimated_date_time(self):
        """Gets the estimated_date_time of this RandomForestOptimizationStatus.  # noqa: E501

        Optimization estimated finish date and time  # noqa: E501

        :return: The estimated_date_time of this RandomForestOptimizationStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._estimated_date_time

    @estimated_date_time.setter
    def estimated_date_time(self, estimated_date_time):
        """Sets the estimated_date_time of this RandomForestOptimizationStatus.

        Optimization estimated finish date and time  # noqa: E501

        :param estimated_date_time: The estimated_date_time of this RandomForestOptimizationStatus.  # noqa: E501
        :type: datetime
        """

        self._estimated_date_time = estimated_date_time

    @property
    def generation_seconds(self):
        """Gets the generation_seconds of this RandomForestOptimizationStatus.  # noqa: E501

        How many seconds has this generation worked  # noqa: E501

        :return: The generation_seconds of this RandomForestOptimizationStatus.  # noqa: E501
        :rtype: int
        """
        return self._generation_seconds

    @generation_seconds.setter
    def generation_seconds(self, generation_seconds):
        """Sets the generation_seconds of this RandomForestOptimizationStatus.

        How many seconds has this generation worked  # noqa: E501

        :param generation_seconds: The generation_seconds of this RandomForestOptimizationStatus.  # noqa: E501
        :type: int
        """

        self._generation_seconds = generation_seconds

    @property
    def metric_name(self):
        """Gets the metric_name of this RandomForestOptimizationStatus.  # noqa: E501

        Metric name  # noqa: E501

        :return: The metric_name of this RandomForestOptimizationStatus.  # noqa: E501
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this RandomForestOptimizationStatus.

        Metric name  # noqa: E501

        :param metric_name: The metric_name of this RandomForestOptimizationStatus.  # noqa: E501
        :type: str
        """

        self._metric_name = metric_name

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
        if not isinstance(other, RandomForestOptimizationStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RandomForestOptimizationStatus):
            return True

        return self.to_dict() != other.to_dict()
