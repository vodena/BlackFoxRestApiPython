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
**best_model** | [**RandomForestOptimizedModel**](RandomForestOptimizedModel.md) | Best model, only set if optimization is finished | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


