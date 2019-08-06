# blackfox_restapi.RecurrentOptimizationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_status**](RecurrentOptimizationApi.md#get_status) | **GET** /api/optimization/rnn/keras/{id}/status | 
[**post**](RecurrentOptimizationApi.md#post) | **POST** /api/optimization/rnn/keras | 
[**post_action**](RecurrentOptimizationApi.md#post_action) | **POST** /api/optimization/rnn/keras/{id}/action/{optimizationAction} | 


# **get_status**
> KerasRecurrentOptimizationStatus get_status(id)



### Example
```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blackfox_restapi.RecurrentOptimizationApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.get_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurrentOptimizationApi->get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**KerasRecurrentOptimizationStatus**](KerasRecurrentOptimizationStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post**
> str post(config=config)



### Example
```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blackfox_restapi.RecurrentOptimizationApi()
config = blackfox_restapi.KerasRecurrentOptimizationConfig() # KerasRecurrentOptimizationConfig |  (optional)

try:
    api_response = api_instance.post(config=config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurrentOptimizationApi->post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | [**KerasRecurrentOptimizationConfig**](KerasRecurrentOptimizationConfig.md)|  | [optional] 

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



### Example
```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blackfox_restapi.RecurrentOptimizationApi()
id = 'id_example' # str | 
optimization_action = 'optimization_action_example' # str | 

try:
    api_instance.post_action(id, optimization_action)
except ApiException as e:
    print("Exception when calling RecurrentOptimizationApi->post_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **optimization_action** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

