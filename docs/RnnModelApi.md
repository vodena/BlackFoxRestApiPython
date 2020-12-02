# blackfox_restapi.RnnModelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download**](RnnModelApi.md#download) | **GET** /api/rnn/model/{id} | Download model file
[**exists**](RnnModelApi.md#exists) | **HEAD** /api/rnn/model/{id} | Check if model file exist
[**get_metadata**](RnnModelApi.md#get_metadata) | **GET** /api/rnn/model/{id}/metadata | Get model metadata
[**upload**](RnnModelApi.md#upload) | **POST** /api/rnn/model | Upload model file


# **download**
> file download(id, integrate_scaler=integrate_scaler, model_type=model_type)

Download model file

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
    api_instance = blackfox_restapi.RnnModelApi(api_client)
    id = 'id_example' # str | File hash(sha1)
integrate_scaler = False # bool | Integrate scaler in model (optional) (default to False)
model_type = blackfox_restapi.NeuralNetworkType() # NeuralNetworkType | h5, onnx, pb (optional)

    try:
        # Download model file
        api_response = api_instance.download(id, integrate_scaler=integrate_scaler, model_type=model_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RnnModelApi->download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File hash(sha1) | 
 **integrate_scaler** | **bool**| Integrate scaler in model | [optional] [default to False]
 **model_type** | [**NeuralNetworkType**](.md)| h5, onnx, pb | [optional] 

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

Check if model file exist

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
    api_instance = blackfox_restapi.RnnModelApi(api_client)
    id = 'id_example' # str | Model Id (sha1)

    try:
        # Check if model file exist
        api_instance.exists(id)
    except ApiException as e:
        print("Exception when calling RnnModelApi->exists: %s\n" % e)
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
    api_instance = blackfox_restapi.RnnModelApi(api_client)
    id = 'id_example' # str | Model Id (sha1)

    try:
        # Get model metadata
        api_response = api_instance.get_metadata(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RnnModelApi->get_metadata: %s\n" % e)
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

Upload model file

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
    api_instance = blackfox_restapi.RnnModelApi(api_client)
    file = '/path/to/file' # file |  (optional)

    try:
        # Upload model file
        api_response = api_instance.upload(file=file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RnnModelApi->upload: %s\n" % e)
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

