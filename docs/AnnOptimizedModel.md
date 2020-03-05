# AnnOptimizedModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Model id | [optional] 
**hidden_layers** | [**list[AnnHiddenLayerConfig]**](AnnHiddenLayerConfig.md) | List of hidden layers | [optional] 
**training_algorithm** | [**AnnTrainingAlgorithm**](AnnTrainingAlgorithm.md) | Algorithm on which model was trained | [optional] 
**output_layer_activation_function** | [**AnnActivationFunction**](AnnActivationFunction.md) | Activation function on output layer | [optional] 
**feature_selection** | **list[bool]** | А bool value for each input indicating whether that input is significant | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

