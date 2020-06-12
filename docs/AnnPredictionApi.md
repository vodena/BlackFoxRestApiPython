# blackfox_restapi.AnnPredictionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**predict_from_array**](AnnPredictionApi.md#predict_from_array) | **POST** /api/ann/prediction/array | Predict values from array
[**predict_from_file**](AnnPredictionApi.md#predict_from_file) | **POST** /api/ann/prediction/file | Predict values from file


# **predict_from_array**
> list[list[float]] predict_from_array(prediction_array_config=prediction_array_config)

Predict values from array

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
    api_instance = blackfox_restapi.AnnPredictionApi(api_client)
    prediction_array_config = blackfox_restapi.PredictionArrayConfig() # PredictionArrayConfig | PredictionArrayConfig (optional)

    try:
        # Predict values from array
        api_response = api_instance.predict_from_array(prediction_array_config=prediction_array_config)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnPredictionApi->predict_from_array: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prediction_array_config** | [**PredictionArrayConfig**](PredictionArrayConfig.md)| PredictionArrayConfig | [optional] 

### Return type

**list[list[float]]**

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

# **predict_from_file**
> str predict_from_file(prediction_file_config=prediction_file_config)

Predict values from file

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
    api_instance = blackfox_restapi.AnnPredictionApi(api_client)
    prediction_file_config = blackfox_restapi.PredictionFileConfig() # PredictionFileConfig |  (optional)

    try:
        # Predict values from file
        api_response = api_instance.predict_from_file(prediction_file_config=prediction_file_config)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnPredictionApi->predict_from_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prediction_file_config** | [**PredictionFileConfig**](PredictionFileConfig.md)|  | [optional] 

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

