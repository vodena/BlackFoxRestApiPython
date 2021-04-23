# AnnSeriesOptimizationConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_window_range_configs** | [**list[InputWindowRangeConfig]**](InputWindowRangeConfig.md) |  | [optional] 
**output_window_configs** | [**list[OutputWindowConfig]**](OutputWindowConfig.md) |  | [optional] 
**output_sample_step** | **int** |  | [optional] [default to 1]
**dropout** | [**Range**](Range.md) |  | [optional] 
**batch_size** | **int** |  | [optional] [default to 512]
**dataset_id** | **str** | Data set id on which to train network | [optional] 
**validation_set_id** | **str** | Data set id on which to validate network | [optional] 
**inputs** | [**list[InputConfig]**](InputConfig.md) | Define min and max value for each output column(feature), and is input optional | [optional] 
**outputs** | [**list[OutputConfig]**](OutputConfig.md) | Define min and max value for each output column(feature) | [optional] 
**problem_type** | [**ProblemType**](ProblemType.md) | Defines the problem type. In case of binary classification,  there must be only one output column. | [optional] 
**binary_optimization_metric** | [**BinaryMetric**](BinaryMetric.md) | USED ONLY IN BINARY CLASSIFICATION.  Default metric: ROC_AUC (Area under ROC curve).   Depending on the task at hand, it is recommended to choose an appropriate metric to optimize. | [optional] 
**regression_optimization_metric** | [**RegressionMetric**](RegressionMetric.md) | USED ONLY IN REGRESSION.  Default metric: MAE (MEAN ABSOLUTE ERROR).   Depending on the task at hand, it is recommended to choose an appropriate metric to optimize. | [optional] 
**hidden_layer_count_range** | [**RangeInt**](RangeInt.md) | Range in which to search number of hidden layers | [optional] 
**neurons_per_layer** | [**RangeInt**](RangeInt.md) | Range in which to search number of neurons per layer | [optional] 
**training_algorithms** | [**list[NeuralNetworkTrainingAlgorithm]**](NeuralNetworkTrainingAlgorithm.md) | List of training algorithms to use | [optional] [default to ["Adadelta","Adagrad","Adam","Adamax","Nadam","RMSprop","SGD"]]
**activation_functions** | [**list[NeuralNetworkActivationFunction]**](NeuralNetworkActivationFunction.md) | List of activation functions to use | [optional] [default to ["Elu","HardSigmoid","Linear","ReLu","Selu","Sigmoid","SoftMax","SoftPlus","SoftSign","TanH"]]
**max_epoch** | **int** | Maximum number of epoch | [default to 3000]
**cross_validation** | **bool** | Use cross validation | [optional] [default to False]
**validation_split** | **float** | Portion of data set to use for validation, must be between 0 and 1.   Used only when CrossValidation &#x3D; false. | [default to 0.2]
**random_seed** | **int** | Random number generator seed, if the value is zero, the rows will not be randomly shuffled  Used only if CrossValidation &#x3D; false | [optional] [default to 300]
**engine_config** | [**AnnOptimizationEngineConfig**](AnnOptimizationEngineConfig.md) | Optimization engine config | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


