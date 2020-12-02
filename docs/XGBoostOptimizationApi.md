# blackfox_restapi.XGBoostOptimizationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](XGBoostOptimizationApi.md#delete) | **DELETE** /api/xgboost/{id} | Delete optimization from optimization service
[**get_model_id**](XGBoostOptimizationApi.md#get_model_id) | **GET** /api/xgboost/{id}/model-id/{generation} | Get id of best model for given generation
[**get_status**](XGBoostOptimizationApi.md#get_status) | **GET** /api/xgboost/{id}/status | Get status of optimization
[**start**](XGBoostOptimizationApi.md#start) | **POST** /api/xgboost | Start XGBoost optimization
[**start_series**](XGBoostOptimizationApi.md#start_series) | **POST** /api/xgboost/series | Starts new series optimization using XGBoost model
[**stop**](XGBoostOptimizationApi.md#stop) | **POST** /api/xgboost/{id}/action/stop | Stop running optimization


# **delete**
> delete(id)

Delete optimization from optimization service

### Example

```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = blackfox_restapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with blackfox_restapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = blackfox_restapi.XGBoostOptimizationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete optimization from optimization service
        api_instance.delete(id)
    except ApiException as e:
        print("Exception when calling XGBoostOptimizationApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

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
**200** | Success |  -  |
**500** | Server Error |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_id**
> str get_model_id(id, generation)

Get id of best model for given generation

### Example

```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = blackfox_restapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with blackfox_restapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = blackfox_restapi.XGBoostOptimizationApi(api_client)
    id = 'id_example' # str | optimization id
generation = 56 # int | generation

    try:
        # Get id of best model for given generation
        api_response = api_instance.get_model_id(id, generation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XGBoostOptimizationApi->get_model_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| optimization id | 
 **generation** | **int**| generation | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> list[XGBoostOptimizationStatus] get_status(id)

Get status of optimization

### Example

```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = blackfox_restapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with blackfox_restapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = blackfox_restapi.XGBoostOptimizationApi(api_client)
    id = 'id_example' # str | Optimization Id

    try:
        # Get status of optimization
        api_response = api_instance.get_status(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XGBoostOptimizationApi->get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Optimization Id | 

### Return type

[**list[XGBoostOptimizationStatus]**](XGBoostOptimizationStatus.md)

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
> str start(xg_boost_optimization_config=xg_boost_optimization_config)

Start XGBoost optimization

### Example

```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = blackfox_restapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with blackfox_restapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = blackfox_restapi.XGBoostOptimizationApi(api_client)
    xg_boost_optimization_config = blackfox_restapi.XGBoostOptimizationConfig() # XGBoostOptimizationConfig | XGBoostOptimizationConfig (optional)

    try:
        # Start XGBoost optimization
        api_response = api_instance.start(xg_boost_optimization_config=xg_boost_optimization_config)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XGBoostOptimizationApi->start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xg_boost_optimization_config** | [**XGBoostOptimizationConfig**](XGBoostOptimizationConfig.md)| XGBoostOptimizationConfig | [optional] 

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
> str start_series(xg_boost_series_optimization_config=xg_boost_series_optimization_config)

Starts new series optimization using XGBoost model

### Example

```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = blackfox_restapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with blackfox_restapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = blackfox_restapi.XGBoostOptimizationApi(api_client)
    xg_boost_series_optimization_config = blackfox_restapi.XGBoostSeriesOptimizationConfig() # XGBoostSeriesOptimizationConfig | XGBoostSeriesOptimizationConfig (optional)

    try:
        # Starts new series optimization using XGBoost model
        api_response = api_instance.start_series(xg_boost_series_optimization_config=xg_boost_series_optimization_config)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XGBoostOptimizationApi->start_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xg_boost_series_optimization_config** | [**XGBoostSeriesOptimizationConfig**](XGBoostSeriesOptimizationConfig.md)| XGBoostSeriesOptimizationConfig | [optional] 

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
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = blackfox_restapi.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with blackfox_restapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = blackfox_restapi.XGBoostOptimizationApi(api_client)
    id = 'id_example' # str | Optimization Id

    try:
        # Stop running optimization
        api_instance.stop(id)
    except ApiException as e:
        print("Exception when calling XGBoostOptimizationApi->stop: %s\n" % e)
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

