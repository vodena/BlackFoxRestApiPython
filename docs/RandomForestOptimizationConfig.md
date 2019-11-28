# RandomForestOptimizationConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** | Data set id on which to train network | [optional] 
**inputs** | [**list[InputConfig]**](InputConfig.md) | Define min and max value for each output column(feature), and is input optional | [optional] 
**output_ranges** | [**list[Range]**](Range.md) | Define min and max value for each output column(feature) | [optional] 
**problem_type** | **str** | Defines the problem type. In case of binary classification,  there must be only one output column. | [optional] 
**validation_split** | **float** | Portion of data set to use for validation, must be between 0 and 1.   Used only when CrossValidation &#x3D; false. | 
**random_seed** | **int** | Random number generator seed, if the value is zero, the rows will not be randomly shuffled  Used only if CrossValidation &#x3D; false | [optional] 
**engine_config** | [**RecurrentOptimizationEngineConfig**](RecurrentOptimizationEngineConfig.md) | Optimization engine config | [optional] 
**number_of_estimators** | [**Range**](Range.md) |  | 
**max_depth** | [**Range**](Range.md) |  | 
**max_features** | [**Range**](Range.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


