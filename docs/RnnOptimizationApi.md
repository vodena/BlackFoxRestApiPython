# blackfox_restapi.RnnOptimizationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_status**](RnnOptimizationApi.md#get_status) | **GET** /api/rnn/{id}/status | Get status of optimization
[**set_action**](RnnOptimizationApi.md#set_action) | **POST** /api/rnn/{id}/action/stop | Stop running optimization
[**start**](RnnOptimizationApi.md#start) | **POST** /api/rnn | Starts new reccurent neural network optimization


# **get_status**
> list[RnnOptimizationStatus] get_status(id)

Get status of optimization

### Example

```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with blackfox_restapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = blackfox_restapi.RnnOptimizationApi(api_client)
    id = 'id_example' # str | Optimization Id

    try:
        # Get status of optimization
        api_response = api_instance.get_status(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RnnOptimizationApi->get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Optimization Id | 

### Return type

[**list[RnnOptimizationStatus]**](RnnOptimizationStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_action**
> set_action(id)

Stop running optimization

### Example

```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with blackfox_restapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = blackfox_restapi.RnnOptimizationApi(api_client)
    id = 'id_example' # str | Optimization Id

    try:
        # Stop running optimization
        api_instance.set_action(id)
    except ApiException as e:
        print("Exception when calling RnnOptimizationApi->set_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Optimization Id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**500** | Internal server error |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start**
> str start(rnn_optimization_config=rnn_optimization_config)

Starts new reccurent neural network optimization

### Example

```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with blackfox_restapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = blackfox_restapi.RnnOptimizationApi(api_client)
    rnn_optimization_config = blackfox_restapi.RnnOptimizationConfig() # RnnOptimizationConfig | RnnOptimizationConfig (optional)

    try:
        # Starts new reccurent neural network optimization
        api_response = api_instance.start(rnn_optimization_config=rnn_optimization_config)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RnnOptimizationApi->start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rnn_optimization_config** | [**RnnOptimizationConfig**](RnnOptimizationConfig.md)| RnnOptimizationConfig | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

