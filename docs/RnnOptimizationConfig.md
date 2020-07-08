# RnnOptimizationConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dropout** | [**Range**](Range.md) |  | [optional] 
**batch_size** | **int** |  | [optional] [default to 512]
**recurrent_dropout** | [**Range**](Range.md) |  | [optional] 
**recurrent_output_count** | **int** |  | [optional] [default to 1]
**dataset_id** | **str** | Data set id on which to train network | [optional] 
**validation_set_id** | **str** | Data set id on which to validate network | [optional] 
**inputs** | [**list[InputConfig]**](InputConfig.md) | Define min and max value for each output column(feature), and is input optional | [optional] 
**output_ranges** | [**list[Range]**](Range.md) | Define min and max value for each output column(feature) | [optional] 
**hidden_layer_count_range** | [**RangeInt**](RangeInt.md) | Range in which to search number of hidden layers | [optional] 
**neurons_per_layer** | [**RangeInt**](RangeInt.md) | Range in which to search number of neurons per layer | [optional] 
**training_algorithms** | [**list[NeuralNetworkTrainingAlgorithm]**](NeuralNetworkTrainingAlgorithm.md) | List of training algorithms to use | [optional] [default to ["Adadelta","Adagrad","Adam","Adamax","Nadam","RMSprop","SGD"]]
**activation_functions** | [**list[NeuralNetworkActivationFunction]**](NeuralNetworkActivationFunction.md) | List of activation functions to use | [optional] [default to ["Elu","HardSigmoid","Linear","ReLu","Selu","Sigmoid","SoftMax","SoftPlus","SoftSign","TanH"]]
**recurrent_activation_functions** | [**list[NeuralNetworkActivationFunction]**](NeuralNetworkActivationFunction.md) | List of recurrent activation functions to use | [optional] [default to ["Elu","HardSigmoid","Linear","ReLu","Selu","Sigmoid","SoftMax","SoftPlus","SoftSign","TanH"]]
**max_epoch** | **int** | Maximum number of epoch | [default to 3000]
**validation_split** | **float** | Portion of data set to use for validation, must be between 0 and 1. | [default to 0.2]
**random_seed** | **int** | Random number generator seed, if the value is zero, the rows will not be randomly shuffled | [optional] [default to 300]
**recurrent_input_count_range** | [**Range**](Range.md) | Range in which to search number of recurrent inputs | [optional] 
**engine_config** | [**OptimizationEngineConfig**](OptimizationEngineConfig.md) | Optimization engine config | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


