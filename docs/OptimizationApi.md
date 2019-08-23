# blackfox_restapi.OptimizationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_status**](OptimizationApi.md#get_status) | **GET** /api/optimization/keras/{id}/status | Get status of optimization
[**post**](OptimizationApi.md#post) | **POST** /api/optimization/keras | Starts new optimization using keras
[**post_action**](OptimizationApi.md#post_action) | **POST** /api/optimization/keras/{id}/action/{optimizationAction} | Stop or cancel running optimization
[**post_series**](OptimizationApi.md#post_series) | **POST** /api/optimization/keras-series | Starts new series optimization using keras


# **get_status**
> KerasOptimizationStatus get_status(id)

Get status of optimization

### Example
```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blackfox_restapi.OptimizationApi()
id = 'id_example' # str | Optimization Id

try:
    # Get status of optimization
    api_response = api_instance.get_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptimizationApi->get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Optimization Id | 

### Return type

[**KerasOptimizationStatus**](KerasOptimizationStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post**
> str post(config=config)

Starts new optimization using keras

### Example
```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blackfox_restapi.OptimizationApi()
config = blackfox_restapi.KerasOptimizationConfig() # KerasOptimizationConfig | KerasOptimizationConfig (optional)

try:
    # Starts new optimization using keras
    api_response = api_instance.post(config=config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptimizationApi->post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | [**KerasOptimizationConfig**](KerasOptimizationConfig.md)| KerasOptimizationConfig | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_action**
> post_action(id, optimization_action)

Stop or cancel running optimization

### Example
```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blackfox_restapi.OptimizationApi()
id = 'id_example' # str | Optimization Id
optimization_action = 'optimization_action_example' # str | Stop, Cancel

try:
    # Stop or cancel running optimization
    api_instance.post_action(id, optimization_action)
except ApiException as e:
    print("Exception when calling OptimizationApi->post_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Optimization Id | 
 **optimization_action** | **str**| Stop, Cancel | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_series**
> str post_series(config=config)

Starts new series optimization using keras

### Example
```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blackfox_restapi.OptimizationApi()
config = blackfox_restapi.KerasSeriesOptimizationConfig() # KerasSeriesOptimizationConfig | KerasSeriesOptimizationConfig (optional)

try:
    # Starts new series optimization using keras
    api_response = api_instance.post_series(config=config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptimizationApi->post_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | [**KerasSeriesOptimizationConfig**](KerasSeriesOptimizationConfig.md)| KerasSeriesOptimizationConfig | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

