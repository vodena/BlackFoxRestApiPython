# blackfox_restapi.InfoApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version**](InfoApi.md#version) | **GET** /api/info/version | 


# **version**
> str version()



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
    api_instance = blackfox_restapi.InfoApi(api_client)
    
    try:
        api_response = api_instance.version()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InfoApi->version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

