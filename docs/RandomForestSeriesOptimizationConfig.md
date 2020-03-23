# RandomForestSeriesOptimizationConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_window_range_configs** | [**list[InputWindowRangeConfig]**](InputWindowRangeConfig.md) |  | [optional] 
**output_window_configs** | [**list[OutputWindowConfig]**](OutputWindowConfig.md) |  | [optional] 
**output_sample_step** | **int** |  | [optional] 
**dataset_id** | **str** | Data set id on which to train model | [optional] 
**inputs** | [**list[InputConfig]**](InputConfig.md) | Define min and max value for each output column(feature), and is input optional | [optional] 
**output_ranges** | [**list[Range]**](Range.md) | Define min and max value for each output column(feature) | [optional] 
**problem_type** | [**ProblemType**](ProblemType.md) | Defines the problem type. In case of binary classification,  there must be only one output column. | [optional] 
**validation_split** | **float** | Portion of data set to use for validation, must be between 0 and 1.   Used only when CrossValidation &#x3D; false. | [default to 0.2]
**random_seed** | **int** | Random number generator seed, if the value is zero, the rows will not be randomly shuffled  Used only if CrossValidation &#x3D; false | [optional] [default to 300]
**engine_config** | [**OptimizationEngineConfig**](OptimizationEngineConfig.md) | Optimization engine config | [optional] 
**number_of_estimators** | [**RangeInt**](RangeInt.md) | Number of estimators | 
**max_depth** | [**RangeInt**](RangeInt.md) | Max depth of tree | 
**max_features** | [**RangeInt**](RangeInt.md) | Max features | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


