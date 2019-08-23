# OptimizationEngineConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optimization_algorithm** | **str** |  | [optional] 
**crossover_distribution_index** | **int** |  | [optional] 
**crossover_probability** | **float** |  | [optional] 
**mutation_distribution_index** | **int** |  | [optional] 
**mutation_probability** | **float** |  | [optional] 
**proc_timeout_seconds** | **int** | Time in seconds in which individual network must finish training.  If not finished in time error will have maximum value. | 
**max_num_of_generations** | **int** | Maximum number of generations in which to find optimal network | [optional] 
**population_size** | **int** | Number of individials in one generation | [optional] 
**hyper_volume** | [**ConvergencyCriterion**](ConvergencyCriterion.md) | Define hyper volume for early stopping | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


