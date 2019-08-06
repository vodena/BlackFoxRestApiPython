# blackfox_restapi.NetworkApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](NetworkApi.md#get) | **GET** /api/network/{id} | Download nework file (*.h5)
[**get_metadata**](NetworkApi.md#get_metadata) | **GET** /api/network/{id}/metadata | Get h5 file metadata
[**head**](NetworkApi.md#head) | **HEAD** /api/network/{id} | Check if h5 file exist
[**post**](NetworkApi.md#post) | **POST** /api/network | Upload h5 file


# **get**
> file get(id, integrate_scaler=integrate_scaler, network_type=network_type)

Download nework file (*.h5)

### Example
```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blackfox_restapi.NetworkApi()
id = 'id_example' # str | Nework Id
integrate_scaler = false # bool |  (optional) (default to false)
network_type = 'h5' # str |  (optional) (default to h5)

try:
    # Download nework file (*.h5)
    api_response = api_instance.get(id, integrate_scaler=integrate_scaler, network_type=network_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Nework Id | 
 **integrate_scaler** | **bool**|  | [optional] [default to false]
 **network_type** | **str**|  | [optional] [default to h5]

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata**
> object get_metadata(id)

Get h5 file metadata

### Example
```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blackfox_restapi.NetworkApi()
id = 'id_example' # str | File hash(sha1)

try:
    # Get h5 file metadata
    api_response = api_instance.get_metadata(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File hash(sha1) | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head**
> head(id)

Check if h5 file exist

### Example
```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blackfox_restapi.NetworkApi()
id = 'id_example' # str | File hash(sha1)

try:
    # Check if h5 file exist
    api_instance.head(id)
except ApiException as e:
    print("Exception when calling NetworkApi->head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File hash(sha1) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post**
> str post(file=file)

Upload h5 file

### Example
```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = blackfox_restapi.NetworkApi()
file = '/path/to/file.txt' # file |  (optional)

try:
    # Upload h5 file
    api_response = api_instance.post(file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->post: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

