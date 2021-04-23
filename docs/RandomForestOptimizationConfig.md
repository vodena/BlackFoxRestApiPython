# RandomForestOptimizationConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** | Data set id on which to train model | [optional] 
**validation_set_id** | **str** | Data set id on which to validate model | [optional] 
**inputs** | [**list[InputConfig]**](InputConfig.md) | Define min and max value for each output column(feature), and is input optional | [optional] 
**outputs** | [**list[OutputConfig]**](OutputConfig.md) | Define min and max value for each output column(feature) | [optional] 
**problem_type** | [**ProblemType**](ProblemType.md) | Defines the problem type. In case of binary classification,  there must be only one output column. | [optional] 
**binary_optimization_metric** | [**BinaryMetric**](BinaryMetric.md) | USED ONLY IN BINARY CLASSIFICATION.  Default metric: ROC_AUC (Area under ROC curve).   Depending on the task at hand, it is recommended to choose an appropriate metric to optimize. | [optional] 
**regression_optimization_metric** | [**RegressionMetric**](RegressionMetric.md) | USED ONLY IN REGRESSION.  Default metric: MAE (MEAN ABSOLUTE ERROR).   Depending on the task at hand, it is recommended to choose an appropriate metric to optimize. | [optional] 
**validation_split** | **float** | Portion of data set to use for validation, must be between 0 and 1.   Used only when CrossValidation &#x3D; false. | [default to 0.2]
**random_seed** | **int** | Random number generator seed, if the value is zero, the rows will not be randomly shuffled  Used only if CrossValidation &#x3D; false | [optional] [default to 300]
**engine_config** | [**OptimizationEngineConfig**](OptimizationEngineConfig.md) | Optimization engine config | [optional] 
**number_of_estimators** | [**RangeInt**](RangeInt.md) | Number of estimators | 
**max_depth** | [**RangeInt**](RangeInt.md) | Max depth of tree | 
**max_features** | [**Range**](Range.md) | Max features | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


