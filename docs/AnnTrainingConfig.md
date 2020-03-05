# AnnTrainingConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_size** | **int** | Training batch size | [optional] 
**dataset_id** | **str** | Data set id on which to train network | [optional] 
**input_ranges** | [**list[Range]**](Range.md) | Define min and max value for each input column(feature) | [optional] 
**output_layer** | [**AnnLayerConfig**](AnnLayerConfig.md) | Define min and max value for each output column(feature), and output activation function | [optional] 
**hidden_layer_configs** | [**list[AnnHiddenLayerConfig]**](AnnHiddenLayerConfig.md) | Hidden layers configuration | [optional] 
**training_algorithm** | [**AnnTrainingAlgorithm**](AnnTrainingAlgorithm.md) | Training algorithm to use | [optional] 
**max_epoch** | **int** | Maximum number of epoch | 
**cross_validation** | **bool** | Use cross validation | [optional] 
**validation_split** | **float** | Portion of data set to use for validation, must be between 0 and 1.   Used only when CrossValidation &#x3D; false. | 
**random_seed** | **int** | Random number generator seed, if the value is zero, the rows will not be randomly shuffled  Used only if CrossValidation &#x3D; false | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


