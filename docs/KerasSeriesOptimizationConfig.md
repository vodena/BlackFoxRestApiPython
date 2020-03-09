# KerasSeriesOptimizationConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_window_range_configs** | [**list[InputWindowRangeConfig]**](InputWindowRangeConfig.md) |  | [optional] 
**output_window_configs** | [**list[OutputWindowConfig]**](OutputWindowConfig.md) |  | [optional] 
**output_sample_step** | **int** |  | [optional] 
**dropout** | [**Range**](Range.md) |  | [optional] 
**batch_size** | **int** |  | [optional] 
**dataset_id** | **str** | Data set id on which to train network | [optional] 
**inputs** | [**list[InputConfig]**](InputConfig.md) | Define min and max value for each output column(feature), and is input optional | [optional] 
**output_ranges** | [**list[Range]**](Range.md) | Define min and max value for each output column(feature) | [optional] 
**problem_type** | **str** | Defines the problem type. In case of binary classification,  there must be only one output column. | [optional] 
**binary_optimization_metric** | **str** | USED ONLY IN BINARY CLASSIFICATION.  Default metric: Auc (Area under ROC curve).   Depending on the task at hand, it is recommended to choose an appropriate metric to optimize. | [optional] 
**hidden_layer_count_range** | [**Range**](Range.md) | Range in which to search number of hidden layers | [optional] 
**neurons_per_layer** | [**Range**](Range.md) | Range in which to search number of neurons per layer | [optional] 
**training_algorithms** | **list[str]** | List of training algorithms to use | [optional] 
**activation_functions** | **list[str]** | List of activation functions to use | [optional] 
**max_epoch** | **int** | Maximum number of epoch | 
**cross_validation** | **bool** | Use cross validation | [optional] 
**validation_split** | **float** | Portion of data set to use for validation, must be between 0 and 1.   Used only when CrossValidation &#x3D; false. | 
**random_seed** | **int** | Random number generator seed, if the value is zero, the rows will not be randomly shuffled  Used only if CrossValidation &#x3D; false | [optional] 
**engine_config** | [**OptimizationEngineConfig**](OptimizationEngineConfig.md) | Optimization engine config | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

