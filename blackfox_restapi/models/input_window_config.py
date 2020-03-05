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


class InputWindowConfig(object):
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
        'step': 'int',
        'aggregation_type': 'AggregationType',
        'window': 'int',
        'shift': 'int'
    }

    attribute_map = {
        'step': 'step',
        'aggregation_type': 'aggregationType',
        'window': 'window',
        'shift': 'shift'
    }

    def __init__(self, step=None, aggregation_type=None, window=None, shift=None, local_vars_configuration=None):  # noqa: E501
        """InputWindowConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._step = None
        self._aggregation_type = None
        self._window = None
        self._shift = None
        self.discriminator = None

        if step is not None:
            self.step = step
        if aggregation_type is not None:
            self.aggregation_type = aggregation_type
        if window is not None:
            self.window = window
        if shift is not None:
            self.shift = shift

    @property
    def step(self):
        """Gets the step of this InputWindowConfig.  # noqa: E501

        Number od values to skip before taking next value  # noqa: E501

        :return: The step of this InputWindowConfig.  # noqa: E501
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this InputWindowConfig.

        Number od values to skip before taking next value  # noqa: E501

        :param step: The step of this InputWindowConfig.  # noqa: E501
        :type: int
        """

        self._step = step

    @property
    def aggregation_type(self):
        """Gets the aggregation_type of this InputWindowConfig.  # noqa: E501

        Aggregation type for values  # noqa: E501

        :return: The aggregation_type of this InputWindowConfig.  # noqa: E501
        :rtype: AggregationType
        """
        return self._aggregation_type

    @aggregation_type.setter
    def aggregation_type(self, aggregation_type):
        """Sets the aggregation_type of this InputWindowConfig.

        Aggregation type for values  # noqa: E501

        :param aggregation_type: The aggregation_type of this InputWindowConfig.  # noqa: E501
        :type: AggregationType
        """

        self._aggregation_type = aggregation_type

    @property
    def window(self):
        """Gets the window of this InputWindowConfig.  # noqa: E501

        Window width, number od values to take  # noqa: E501

        :return: The window of this InputWindowConfig.  # noqa: E501
        :rtype: int
        """
        return self._window

    @window.setter
    def window(self, window):
        """Sets the window of this InputWindowConfig.

        Window width, number od values to take  # noqa: E501

        :param window: The window of this InputWindowConfig.  # noqa: E501
        :type: int
        """

        self._window = window

    @property
    def shift(self):
        """Gets the shift of this InputWindowConfig.  # noqa: E501

        Number of values to skip before taking value.  The negative value skips the data to the left, the positive skips the data to the right.  # noqa: E501

        :return: The shift of this InputWindowConfig.  # noqa: E501
        :rtype: int
        """
        return self._shift

    @shift.setter
    def shift(self, shift):
        """Sets the shift of this InputWindowConfig.

        Number of values to skip before taking value.  The negative value skips the data to the left, the positive skips the data to the right.  # noqa: E501

        :param shift: The shift of this InputWindowConfig.  # noqa: E501
        :type: int
        """

        self._shift = shift

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
        if not isinstance(other, InputWindowConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputWindowConfig):
            return True

        return self.to_dict() != other.to_dict()
