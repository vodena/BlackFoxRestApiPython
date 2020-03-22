# AnnOptimizationEngineConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optimization_algorithm** | [**OptimizationAlgorithm**](OptimizationAlgorithm.md) |  | [optional] 
**crossover_distribution_index** | **int** |  | [optional] 
**crossover_probability** | **float** |  | [optional] 
**mutation_distribution_index** | **int** |  | [optional] 
**mutation_probability** | **float** |  | [optional] 
**proc_timeout_seconds** | **int** | Time in seconds in which individual network must finish training.  If not finished in time error will have maximum value. | [default to 10800]
**max_num_of_generations** | **int** | Maximum number of generations in which to find optimal network | [default to 50]
**population_size** | **int** | Number of individials in one generation | [optional] [default to 50]
**hyper_volume** | [**ConvergencyCriterion**](ConvergencyCriterion.md) | Define hyper volume for early stopping | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


