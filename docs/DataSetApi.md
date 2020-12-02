# blackfox_restapi.DataSetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download**](DataSetApi.md#download) | **GET** /api/dataset/{id} | Download dataset file (*.csv)
[**exists**](DataSetApi.md#exists) | **HEAD** /api/dataset/{id} | Check if dataset file exist
[**upload**](DataSetApi.md#upload) | **POST** /api/dataset | Upload dataset file (*.csv)


# **download**
> file download(id)

Download dataset file (*.csv)

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
    api_instance = blackfox_restapi.DataSetApi(api_client)
    id = 'id_example' # str | Dataset Id

    try:
        # Download dataset file (*.csv)
        api_response = api_instance.download(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataSetApi->download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Dataset Id | 

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
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exists**
> exists(id)

Check if dataset file exist

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
    api_instance = blackfox_restapi.DataSetApi(api_client)
    id = 'id_example' # str | Dataset Id (sha1)

    try:
        # Check if dataset file exist
        api_instance.exists(id)
    except ApiException as e:
        print("Exception when calling DataSetApi->exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Dataset Id (sha1) | 

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

# **upload**
> str upload(file=file)

Upload dataset file (*.csv)

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
    api_instance = blackfox_restapi.DataSetApi(api_client)
    file = '/path/to/file' # file |  (optional)

    try:
        # Upload dataset file (*.csv)
        api_response = api_instance.upload(file=file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DataSetApi->upload: %s\n" % e)
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
**304** | Not Modified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

