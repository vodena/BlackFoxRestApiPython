# blackfox_restapi.XGBoostModelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download**](XGBoostModelApi.md#download) | **GET** /api/xgboost/model/{id} | Download model file (*.bin)
[**exists**](XGBoostModelApi.md#exists) | **HEAD** /api/xgboost/model/{id} | Check if h5 file exist
[**get_metadata**](XGBoostModelApi.md#get_metadata) | **GET** /api/xgboost/model/{id}/metadata | Get model metadata
[**upload**](XGBoostModelApi.md#upload) | **POST** /api/xgboost/model | Upload model(binary file)


# **download**
> file download(id)

Download model file (*.bin)

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
    api_instance = blackfox_restapi.XGBoostModelApi(api_client)
    id = 'id_example' # str | File hash(sha1)

    try:
        # Download model file (*.bin)
        api_response = api_instance.download(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XGBoostModelApi->download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File hash(sha1) | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**404** | Do not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exists**
> exists(id)

Check if h5 file exist

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
    api_instance = blackfox_restapi.XGBoostModelApi(api_client)
    id = 'id_example' # str | Model Id (sha1)

    try:
        # Check if h5 file exist
        api_instance.exists(id)
    except ApiException as e:
        print("Exception when calling XGBoostModelApi->exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model Id (sha1) | 

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
**200** | Exist |  -  |
**404** | Do not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata**
> object get_metadata(id)

Get model metadata

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
    api_instance = blackfox_restapi.XGBoostModelApi(api_client)
    id = 'id_example' # str | Model Id (sha1)

    try:
        # Get model metadata
        api_response = api_instance.get_metadata(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XGBoostModelApi->get_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Model Id (sha1) | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**404** | Do not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload**
> str upload(file=file)

Upload model(binary file)

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
    api_instance = blackfox_restapi.XGBoostModelApi(api_client)
    file = '/path/to/file' # file |  (optional)

    try:
        # Upload model(binary file)
        api_response = api_instance.upload(file=file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XGBoostModelApi->upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**304** | Already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

