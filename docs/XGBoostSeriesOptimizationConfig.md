# XGBoostSeriesOptimizationConfig

Config for data series optimization using XGBoost model
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_window_range_configs** | [**list[InputWindowRangeConfig]**](InputWindowRangeConfig.md) |  | [optional] 
**output_window_configs** | [**list[OutputWindowConfig]**](OutputWindowConfig.md) |  | [optional] 
**output_sample_step** | **int** |  | [optional] 
**dataset_id** | **str** |  | [optional] 
**inputs** | [**list[InputConfig]**](InputConfig.md) |  | [optional] 
**output_ranges** | [**list[Range]**](Range.md) |  | [optional] 
**validation_split** | **float** |  | [optional] 
**random_seed** | **int** |  | [optional] 
**max_depth** | [**RangeInt**](RangeInt.md) | MaxDepth | 
**min_child_weight** | [**RangeInt**](RangeInt.md) | MinChildWeight | 
**gamma** | [**Range**](Range.md) | Gamma | 
**subsample** | [**Range**](Range.md) | Subsample | 
**colsample_bytree** | [**Range**](Range.md) | ColsampleBytree | 
**reg_alpha** | [**Range**](Range.md) | RegAlpha | 
**learning_rate** | [**Range**](Range.md) | LearningRate | 
**engine_config** | [**OptimizationEngineConfig**](OptimizationEngineConfig.md) | Optimization engine config | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


