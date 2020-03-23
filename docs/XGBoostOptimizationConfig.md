# XGBoostOptimizationConfig

Optimization config for XGBoost model
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** |  | [optional] 
**inputs** | [**list[InputConfig]**](InputConfig.md) |  | [optional] 
**output_ranges** | [**list[Range]**](Range.md) |  | [optional] 
**validation_split** | **float** |  | [optional] [default to 0.2]
**random_seed** | **int** |  | [optional] [default to 300]
**problem_type** | [**ProblemType**](ProblemType.md) | Defines the problem type. In case of binary classification,  there must be only one output column. | [optional] 
**max_depth** | [**RangeInt**](RangeInt.md) | MaxDepth | 
**min_child_weight** | [**RangeInt**](RangeInt.md) | MinChildWeight | 
**gamma** | [**Range**](Range.md) | Gamma | 
**subsample** | [**Range**](Range.md) | Subsample | 
**colsample_bytree** | [**Range**](Range.md) | ColsampleBytree | 
**reg_alpha** | [**Range**](Range.md) | RegAlpha | 
**learning_rate** | [**Range**](Range.md) | LearningRate | 
**engine_config** | [**OptimizationEngineConfig**](OptimizationEngineConfig.md) | Optimization engine config | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


