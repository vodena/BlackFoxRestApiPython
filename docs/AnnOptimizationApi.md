# blackfox_restapi.AnnOptimizationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_status**](AnnOptimizationApi.md#get_status) | **GET** /api/ann/{id}/status | Get status of optimization
[**start**](AnnOptimizationApi.md#start) | **POST** /api/ann | Starts new optimization using ann
[**start_series**](AnnOptimizationApi.md#start_series) | **POST** /api/ann/series | Starts new series optimization using ann
[**stop**](AnnOptimizationApi.md#stop) | **POST** /api/ann/{id}/action/stop | Stop running optimization


# **get_status**
> list[AnnOptimizationStatus] get_status(id)

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
    api_instance = blackfox_restapi.AnnOptimizationApi(api_client)
    id = 'id_example' # str | Optimization Id

    try:
        # Get status of optimization
        api_response = api_instance.get_status(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnOptimizationApi->get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Optimization Id | 

### Return type

[**list[AnnOptimizationStatus]**](AnnOptimizationStatus.md)

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

# **start**
> str start(ann_optimization_config=ann_optimization_config)

Starts new optimization using ann

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
    api_instance = blackfox_restapi.AnnOptimizationApi(api_client)
    ann_optimization_config = blackfox_restapi.AnnOptimizationConfig() # AnnOptimizationConfig | AnnOptimizationConfig (optional)

    try:
        # Starts new optimization using ann
        api_response = api_instance.start(ann_optimization_config=ann_optimization_config)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnOptimizationApi->start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ann_optimization_config** | [**AnnOptimizationConfig**](AnnOptimizationConfig.md)| AnnOptimizationConfig | [optional] 

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
> str start_series(ann_series_optimization_config=ann_series_optimization_config)

Starts new series optimization using ann

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
    api_instance = blackfox_restapi.AnnOptimizationApi(api_client)
    ann_series_optimization_config = blackfox_restapi.AnnSeriesOptimizationConfig() # AnnSeriesOptimizationConfig |  (optional)

    try:
        # Starts new series optimization using ann
        api_response = api_instance.start_series(ann_series_optimization_config=ann_series_optimization_config)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnOptimizationApi->start_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ann_series_optimization_config** | [**AnnSeriesOptimizationConfig**](AnnSeriesOptimizationConfig.md)|  | [optional] 

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

# **stop**
> stop(id)

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
    api_instance = blackfox_restapi.AnnOptimizationApi(api_client)
    id = 'id_example' # str | Optimization Id

    try:
        # Stop running optimization
        api_instance.stop(id)
    except ApiException as e:
        print("Exception when calling AnnOptimizationApi->stop: %s\n" % e)
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

