# RandomForestOptimizationStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_selection** | **list[bool]** | А bool value for each input indicating whether that input is significant | [optional] 
**guid** | **str** | Guid | [optional] 
**state** | [**OptimizationState**](OptimizationState.md) | Optimization state (Active, Finished, Stopped, Error) | [optional] 
**generation** | **int** | Current generation | [optional] 
**total_generations** | **int** | Total number of generations | [optional] 
**validation_set_error** | **float** | Error on validation set | [optional] 
**training_set_error** | **float** | Error on training set | [optional] 
**best_model** | [**RandomForestModel**](RandomForestModel.md) | Best model, only set if optimization is finished | [optional] 
**start_date_time** | **datetime** | Optimization start date and time | [optional] 
**estimated_date_time** | **datetime** | Optimization estimated finish date and time | [optional] 
**generation_seconds** | **int** | How many seconds has this generation worked | [optional] 
**metric_name** | **str** | Metric name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


