# blackfox_restapi.RandomForestOptimizationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_status**](RandomForestOptimizationApi.md#get_status) | **GET** /api/random-forest/{id}/status | Get status of optimization
[**set_action**](RandomForestOptimizationApi.md#set_action) | **POST** /api/random-forest/{id}/action/{optimizationAction} | Stop or cancel running optimization
[**start**](RandomForestOptimizationApi.md#start) | **POST** /api/random-forest | Starts new optimization using random forest
[**start_series**](RandomForestOptimizationApi.md#start_series) | **POST** /api/random-forest/series | Starts new series optimization using random forest


# **get_status**
> list[RandomForestOptimizationStatus] get_status(id)

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
    api_instance = blackfox_restapi.RandomForestOptimizationApi(api_client)
    id = 'id_example' # str | Optimization Id

    try:
        # Get status of optimization
        api_response = api_instance.get_status(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RandomForestOptimizationApi->get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Optimization Id | 

### Return type

[**list[RandomForestOptimizationStatus]**](RandomForestOptimizationStatus.md)

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
> set_action(id, optimization_action)

Stop or cancel running optimization

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
    api_instance = blackfox_restapi.RandomForestOptimizationApi(api_client)
    id = 'id_example' # str | Optimization Id
optimization_action = blackfox_restapi.OptimizationAction() # OptimizationAction | Stop, Cancel

    try:
        # Stop or cancel running optimization
        api_instance.set_action(id, optimization_action)
    except ApiException as e:
        print("Exception when calling RandomForestOptimizationApi->set_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Optimization Id | 
 **optimization_action** | [**OptimizationAction**](.md)| Stop, Cancel | 

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
> str start(random_forest_optimization_config=random_forest_optimization_config)

Starts new optimization using random forest

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
    api_instance = blackfox_restapi.RandomForestOptimizationApi(api_client)
    random_forest_optimization_config = blackfox_restapi.RandomForestOptimizationConfig() # RandomForestOptimizationConfig | RandomForestOptimizationConfig (optional)

    try:
        # Starts new optimization using random forest
        api_response = api_instance.start(random_forest_optimization_config=random_forest_optimization_config)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RandomForestOptimizationApi->start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **random_forest_optimization_config** | [**RandomForestOptimizationConfig**](RandomForestOptimizationConfig.md)| RandomForestOptimizationConfig | [optional] 

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

# **start_series**
> str start_series(random_forest_series_optimization_config=random_forest_series_optimization_config)

Starts new series optimization using random forest

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
    api_instance = blackfox_restapi.RandomForestOptimizationApi(api_client)
    random_forest_series_optimization_config = blackfox_restapi.RandomForestSeriesOptimizationConfig() # RandomForestSeriesOptimizationConfig | RandomForestSeriesOptimizationConfig (optional)

    try:
        # Starts new series optimization using random forest
        api_response = api_instance.start_series(random_forest_series_optimization_config=random_forest_series_optimization_config)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RandomForestOptimizationApi->start_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **random_forest_series_optimization_config** | [**RandomForestSeriesOptimizationConfig**](RandomForestSeriesOptimizationConfig.md)| RandomForestSeriesOptimizationConfig | [optional] 

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

