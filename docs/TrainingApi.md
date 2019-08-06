# blackfox_restapi.TrainingApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post**](TrainingApi.md#post) | **POST** /api/training/keras | 
[**post_series**](TrainingApi.md#post_series) | **POST** /api/training/keras-series | 


# **post**
> TrainedNetwork post(value=value)



### Example
```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blackfox_restapi.TrainingApi()
value = blackfox_restapi.KerasTrainingConfig() # KerasTrainingConfig |  (optional)

try:
    api_response = api_instance.post(value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrainingApi->post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | [**KerasTrainingConfig**](KerasTrainingConfig.md)|  | [optional] 

### Return type

[**TrainedNetwork**](TrainedNetwork.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_series**
> TrainedNetwork post_series(value=value)



### Example
```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blackfox_restapi.TrainingApi()
value = blackfox_restapi.KerasSeriesTrainingConfig() # KerasSeriesTrainingConfig |  (optional)

try:
    api_response = api_instance.post_series(value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrainingApi->post_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | [**KerasSeriesTrainingConfig**](KerasSeriesTrainingConfig.md)|  | [optional] 

### Return type

[**TrainedNetwork**](TrainedNetwork.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

