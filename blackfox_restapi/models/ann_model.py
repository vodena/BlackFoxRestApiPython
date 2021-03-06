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


class AnnModel(object):
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
        'hidden_layers': 'list[AnnHiddenLayerConfig]',
        'training_algorithm': 'NeuralNetworkTrainingAlgorithm',
        'output_layer_activation_function': 'NeuralNetworkActivationFunction',
        'feature_selection': 'list[bool]'
    }

    attribute_map = {
        'hidden_layers': 'hiddenLayers',
        'training_algorithm': 'trainingAlgorithm',
        'output_layer_activation_function': 'outputLayerActivationFunction',
        'feature_selection': 'featureSelection'
    }

    def __init__(self, hidden_layers=None, training_algorithm=None, output_layer_activation_function=None, feature_selection=None, local_vars_configuration=None):  # noqa: E501
        """AnnModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hidden_layers = None
        self._training_algorithm = None
        self._output_layer_activation_function = None
        self._feature_selection = None
        self.discriminator = None

        self.hidden_layers = hidden_layers
        if training_algorithm is not None:
            self.training_algorithm = training_algorithm
        if output_layer_activation_function is not None:
            self.output_layer_activation_function = output_layer_activation_function
        self.feature_selection = feature_selection

    @property
    def hidden_layers(self):
        """Gets the hidden_layers of this AnnModel.  # noqa: E501

        List of hidden layers  # noqa: E501

        :return: The hidden_layers of this AnnModel.  # noqa: E501
        :rtype: list[AnnHiddenLayerConfig]
        """
        return self._hidden_layers

    @hidden_layers.setter
    def hidden_layers(self, hidden_layers):
        """Sets the hidden_layers of this AnnModel.

        List of hidden layers  # noqa: E501

        :param hidden_layers: The hidden_layers of this AnnModel.  # noqa: E501
        :type: list[AnnHiddenLayerConfig]
        """

        self._hidden_layers = hidden_layers

    @property
    def training_algorithm(self):
        """Gets the training_algorithm of this AnnModel.  # noqa: E501

        Algorithm on which model was trained  # noqa: E501

        :return: The training_algorithm of this AnnModel.  # noqa: E501
        :rtype: NeuralNetworkTrainingAlgorithm
        """
        return self._training_algorithm

    @training_algorithm.setter
    def training_algorithm(self, training_algorithm):
        """Sets the training_algorithm of this AnnModel.

        Algorithm on which model was trained  # noqa: E501

        :param training_algorithm: The training_algorithm of this AnnModel.  # noqa: E501
        :type: NeuralNetworkTrainingAlgorithm
        """

        self._training_algorithm = training_algorithm

    @property
    def output_layer_activation_function(self):
        """Gets the output_layer_activation_function of this AnnModel.  # noqa: E501

        Activation function on output layer  # noqa: E501

        :return: The output_layer_activation_function of this AnnModel.  # noqa: E501
        :rtype: NeuralNetworkActivationFunction
        """
        return self._output_layer_activation_function

    @output_layer_activation_function.setter
    def output_layer_activation_function(self, output_layer_activation_function):
        """Sets the output_layer_activation_function of this AnnModel.

        Activation function on output layer  # noqa: E501

        :param output_layer_activation_function: The output_layer_activation_function of this AnnModel.  # noqa: E501
        :type: NeuralNetworkActivationFunction
        """

        self._output_layer_activation_function = output_layer_activation_function

    @property
    def feature_selection(self):
        """Gets the feature_selection of this AnnModel.  # noqa: E501

        А bool value for each input indicating whether that input is significant  # noqa: E501

        :return: The feature_selection of this AnnModel.  # noqa: E501
        :rtype: list[bool]
        """
        return self._feature_selection

    @feature_selection.setter
    def feature_selection(self, feature_selection):
        """Sets the feature_selection of this AnnModel.

        А bool value for each input indicating whether that input is significant  # noqa: E501

        :param feature_selection: The feature_selection of this AnnModel.  # noqa: E501
        :type: list[bool]
        """

        self._feature_selection = feature_selection

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
        if not isinstance(other, AnnModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnnModel):
            return True

        return self.to_dict() != other.to_dict()
