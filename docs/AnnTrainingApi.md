# blackfox_restapi.AnnTrainingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**train**](AnnTrainingApi.md#train) | **POST** /api/ann/train | 
[**train_series**](AnnTrainingApi.md#train_series) | **POST** /api/ann/train/series | 


# **train**
> TrainedNetwork train(ann_training_config=ann_training_config)



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
    api_instance = blackfox_restapi.AnnTrainingApi(api_client)
    ann_training_config = blackfox_restapi.AnnTrainingConfig() # AnnTrainingConfig |  (optional)

    try:
        api_response = api_instance.train(ann_training_config=ann_training_config)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnTrainingApi->train: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ann_training_config** | [**AnnTrainingConfig**](AnnTrainingConfig.md)|  | [optional] 

### Return type

[**TrainedNetwork**](TrainedNetwork.md)

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

# **train_series**
> TrainedNetwork train_series(ann_series_training_config=ann_series_training_config)



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
    api_instance = blackfox_restapi.AnnTrainingApi(api_client)
    ann_series_training_config = blackfox_restapi.AnnSeriesTrainingConfig() # AnnSeriesTrainingConfig |  (optional)

    try:
        api_response = api_instance.train_series(ann_series_training_config=ann_series_training_config)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnTrainingApi->train_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ann_series_training_config** | [**AnnSeriesTrainingConfig**](AnnSeriesTrainingConfig.md)|  | [optional] 

### Return type

[**TrainedNetwork**](TrainedNetwork.md)

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

