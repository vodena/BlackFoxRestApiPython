# InputWindowConfig

Series input column configuration
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step** | **int** | Number od values to skip before taking next value | [optional] [default to 1]
**aggregation_type** | [**AggregationType**](AggregationType.md) | Aggregation type for values | [optional] 
**window** | **int** | Window width, number od values to take | [optional] [default to 1]
**shift** | **int** | Number of values to skip before taking value.  The negative value skips the data to the left, the positive skips the data to the right. | [optional] [default to 0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


