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

from blackfox_restapi.models.range import Range  # noqa: F401,E501


class PredictionArrayConfig(object):
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
        'data_set': 'list[list[float]]',
        'network_id': 'str',
        'input_ranges': 'list[Range]',
        'output_ranges': 'list[Range]'
    }

    attribute_map = {
        'data_set': 'dataSet',
        'network_id': 'networkId',
        'input_ranges': 'inputRanges',
        'output_ranges': 'outputRanges'
    }

    def __init__(self, data_set=None, network_id=None, input_ranges=None, output_ranges=None):  # noqa: E501
        """PredictionArrayConfig - a model defined in Swagger"""  # noqa: E501

        self._data_set = None
        self._network_id = None
        self._input_ranges = None
        self._output_ranges = None
        self.discriminator = None

        if data_set is not None:
            self.data_set = data_set
        if network_id is not None:
            self.network_id = network_id
        if input_ranges is not None:
            self.input_ranges = input_ranges
        if output_ranges is not None:
            self.output_ranges = output_ranges

    @property
    def data_set(self):
        """Gets the data_set of this PredictionArrayConfig.  # noqa: E501


        :return: The data_set of this PredictionArrayConfig.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._data_set

    @data_set.setter
    def data_set(self, data_set):
        """Sets the data_set of this PredictionArrayConfig.


        :param data_set: The data_set of this PredictionArrayConfig.  # noqa: E501
        :type: list[list[float]]
        """

        self._data_set = data_set

    @property
    def network_id(self):
        """Gets the network_id of this PredictionArrayConfig.  # noqa: E501


        :return: The network_id of this PredictionArrayConfig.  # noqa: E501
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this PredictionArrayConfig.


        :param network_id: The network_id of this PredictionArrayConfig.  # noqa: E501
        :type: str
        """

        self._network_id = network_id

    @property
    def input_ranges(self):
        """Gets the input_ranges of this PredictionArrayConfig.  # noqa: E501


        :return: The input_ranges of this PredictionArrayConfig.  # noqa: E501
        :rtype: list[Range]
        """
        return self._input_ranges

    @input_ranges.setter
    def input_ranges(self, input_ranges):
        """Sets the input_ranges of this PredictionArrayConfig.


        :param input_ranges: The input_ranges of this PredictionArrayConfig.  # noqa: E501
        :type: list[Range]
        """

        self._input_ranges = input_ranges

    @property
    def output_ranges(self):
        """Gets the output_ranges of this PredictionArrayConfig.  # noqa: E501


        :return: The output_ranges of this PredictionArrayConfig.  # noqa: E501
        :rtype: list[Range]
        """
        return self._output_ranges

    @output_ranges.setter
    def output_ranges(self, output_ranges):
        """Sets the output_ranges of this PredictionArrayConfig.


        :param output_ranges: The output_ranges of this PredictionArrayConfig.  # noqa: E501
        :type: list[Range]
        """

        self._output_ranges = output_ranges

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PredictionArrayConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
