# blackfox-restapi

- API version: v1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/vodena/BlackFoxRestApiPython.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import blackfox_restapi
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import blackfox_restapi
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import blackfox_restapi
from blackfox_restapi.rest import ApiException
from pprint import pprint


# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with blackfox_restapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = blackfox_restapi.AnnModelApi(api_client)
    id = 'id_example' # str | File hash(sha1)
integrate_scaler = False # bool | Integrate scaler in model (optional) (default to False)
model_type = blackfox_restapi.NeuralNetworkType() # NeuralNetworkType | h5, onnx, pb (optional)

    try:
        # Download model file
        api_response = api_instance.download(id, integrate_scaler=integrate_scaler, model_type=model_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnModelApi->download: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnnModelApi* | [**download**](docs/AnnModelApi.md#download) | **GET** /api/ann/model/{id} | Download model file
*AnnModelApi* | [**exists**](docs/AnnModelApi.md#exists) | **HEAD** /api/ann/model/{id} | Check if model file exist
*AnnModelApi* | [**get_metadata**](docs/AnnModelApi.md#get_metadata) | **GET** /api/ann/model/{id}/metadata | Get model metadata
*AnnModelApi* | [**upload**](docs/AnnModelApi.md#upload) | **POST** /api/ann/model | Upload model file
*AnnOptimizationApi* | [**delete**](docs/AnnOptimizationApi.md#delete) | **DELETE** /api/ann/{id} | 
*AnnOptimizationApi* | [**get_model_id**](docs/AnnOptimizationApi.md#get_model_id) | **GET** /api/ann/{id}/model-id/{generation} | Get id of best model for given generation index
*AnnOptimizationApi* | [**get_status**](docs/AnnOptimizationApi.md#get_status) | **GET** /api/ann/{id}/status | Get status of optimization
*AnnOptimizationApi* | [**start**](docs/AnnOptimizationApi.md#start) | **POST** /api/ann | Starts new optimization using ann
*AnnOptimizationApi* | [**start_series**](docs/AnnOptimizationApi.md#start_series) | **POST** /api/ann/series | Starts new series optimization using ann
*AnnOptimizationApi* | [**stop**](docs/AnnOptimizationApi.md#stop) | **POST** /api/ann/{id}/action/stop | Stop running optimization
*AnnPredictionApi* | [**predict_from_array**](docs/AnnPredictionApi.md#predict_from_array) | **POST** /api/ann/prediction/array | Predict values from array
*AnnPredictionApi* | [**predict_from_file**](docs/AnnPredictionApi.md#predict_from_file) | **POST** /api/ann/prediction/file | Predict values from file
*AnnTrainingApi* | [**train**](docs/AnnTrainingApi.md#train) | **POST** /api/ann/train | 
*AnnTrainingApi* | [**train_series**](docs/AnnTrainingApi.md#train_series) | **POST** /api/ann/train/series | 
*DataSetApi* | [**download**](docs/DataSetApi.md#download) | **GET** /api/dataset/{id} | Download dataset file (*.csv)
*DataSetApi* | [**exists**](docs/DataSetApi.md#exists) | **HEAD** /api/dataset/{id} | Check if dataset file exist
*DataSetApi* | [**upload**](docs/DataSetApi.md#upload) | **POST** /api/dataset | Upload dataset file (*.csv)
*InfoApi* | [**get**](docs/InfoApi.md#get) | **GET** /api/info | 
*RandomForestModelApi* | [**download**](docs/RandomForestModelApi.md#download) | **GET** /api/random-forest/model/{id} | Download model file (*.h5)
*RandomForestModelApi* | [**exists**](docs/RandomForestModelApi.md#exists) | **HEAD** /api/random-forest/model/{id} | Check if h5 file exist
*RandomForestModelApi* | [**get_metadata**](docs/RandomForestModelApi.md#get_metadata) | **GET** /api/random-forest/model/{id}/metadata | Get model metadata
*RandomForestModelApi* | [**upload**](docs/RandomForestModelApi.md#upload) | **POST** /api/random-forest/model | Upload model(h5 file)
*RandomForestOptimizationApi* | [**delete**](docs/RandomForestOptimizationApi.md#delete) | **DELETE** /api/random-forest/{id} | 
*RandomForestOptimizationApi* | [**get_model_id**](docs/RandomForestOptimizationApi.md#get_model_id) | **GET** /api/random-forest/{id}/model-id/{generation} | 
*RandomForestOptimizationApi* | [**get_status**](docs/RandomForestOptimizationApi.md#get_status) | **GET** /api/random-forest/{id}/status | Get status of optimization
*RandomForestOptimizationApi* | [**start**](docs/RandomForestOptimizationApi.md#start) | **POST** /api/random-forest | Starts new optimization using random forest
*RandomForestOptimizationApi* | [**start_series**](docs/RandomForestOptimizationApi.md#start_series) | **POST** /api/random-forest/series | Starts new series optimization using random forest
*RandomForestOptimizationApi* | [**stop**](docs/RandomForestOptimizationApi.md#stop) | **POST** /api/random-forest/{id}/action/stop | Stop running optimization
*RnnModelApi* | [**download**](docs/RnnModelApi.md#download) | **GET** /api/rnn/model/{id} | Download model file
*RnnModelApi* | [**exists**](docs/RnnModelApi.md#exists) | **HEAD** /api/rnn/model/{id} | Check if model file exist
*RnnModelApi* | [**get_metadata**](docs/RnnModelApi.md#get_metadata) | **GET** /api/rnn/model/{id}/metadata | Get model metadata
*RnnModelApi* | [**upload**](docs/RnnModelApi.md#upload) | **POST** /api/rnn/model | Upload model file
*RnnOptimizationApi* | [**delete**](docs/RnnOptimizationApi.md#delete) | **DELETE** /api/rnn/{id} | 
*RnnOptimizationApi* | [**get_model_id**](docs/RnnOptimizationApi.md#get_model_id) | **GET** /api/rnn/{id}/model-id/{generation} | 
*RnnOptimizationApi* | [**get_status**](docs/RnnOptimizationApi.md#get_status) | **GET** /api/rnn/{id}/status | Get status of optimization
*RnnOptimizationApi* | [**start**](docs/RnnOptimizationApi.md#start) | **POST** /api/rnn | Starts new reccurent neural network optimization
*RnnOptimizationApi* | [**stop**](docs/RnnOptimizationApi.md#stop) | **POST** /api/rnn/{id}/action/stop | Stop running optimization


## Documentation For Models

 - [AggregationType](docs/AggregationType.md)
 - [AnnActivationFunction](docs/AnnActivationFunction.md)
 - [AnnHiddenLayerConfig](docs/AnnHiddenLayerConfig.md)
 - [AnnLayerConfig](docs/AnnLayerConfig.md)
 - [AnnOptimizationConfig](docs/AnnOptimizationConfig.md)
 - [AnnOptimizationEngineConfig](docs/AnnOptimizationEngineConfig.md)
 - [AnnOptimizationStatus](docs/AnnOptimizationStatus.md)
 - [AnnOptimizedModel](docs/AnnOptimizedModel.md)
 - [AnnSeriesOptimizationConfig](docs/AnnSeriesOptimizationConfig.md)
 - [AnnSeriesTrainingConfig](docs/AnnSeriesTrainingConfig.md)
 - [AnnTrainingAlgorithm](docs/AnnTrainingAlgorithm.md)
 - [AnnTrainingConfig](docs/AnnTrainingConfig.md)
 - [ConvergencyCriterion](docs/ConvergencyCriterion.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineObject3](docs/InlineObject3.md)
 - [InputConfig](docs/InputConfig.md)
 - [InputWindowConfig](docs/InputWindowConfig.md)
 - [InputWindowRangeConfig](docs/InputWindowRangeConfig.md)
 - [NeuralNetworkType](docs/NeuralNetworkType.md)
 - [OptimizationAlgorithm](docs/OptimizationAlgorithm.md)
 - [OptimizationEngineConfig](docs/OptimizationEngineConfig.md)
 - [OptimizationState](docs/OptimizationState.md)
 - [OutputWindowConfig](docs/OutputWindowConfig.md)
 - [PredictionArrayConfig](docs/PredictionArrayConfig.md)
 - [PredictionFileConfig](docs/PredictionFileConfig.md)
 - [ProblemDetails](docs/ProblemDetails.md)
 - [ProblemType](docs/ProblemType.md)
 - [RandomForestModelType](docs/RandomForestModelType.md)
 - [RandomForestOptimizationConfig](docs/RandomForestOptimizationConfig.md)
 - [RandomForestOptimizationStatus](docs/RandomForestOptimizationStatus.md)
 - [RandomForestOptimizedModel](docs/RandomForestOptimizedModel.md)
 - [RandomForestSeriesOptimizationConfig](docs/RandomForestSeriesOptimizationConfig.md)
 - [Range](docs/Range.md)
 - [RangeInt](docs/RangeInt.md)
 - [RnnHiddenLayerConfig](docs/RnnHiddenLayerConfig.md)
 - [RnnOptimizationConfig](docs/RnnOptimizationConfig.md)
 - [RnnOptimizationStatus](docs/RnnOptimizationStatus.md)
 - [RnnOptimizedModel](docs/RnnOptimizedModel.md)
 - [ServiceInfo](docs/ServiceInfo.md)
 - [TrainedNetwork](docs/TrainedNetwork.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




