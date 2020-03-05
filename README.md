# blackfox-restapi

- API version: v1
- Package version: 0.0.2

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

Install with 

```sh
pip install BlackFoxRestApiPython
```

If the python package is hosted on Github, you can install directly from Github

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
        # Download model file (*.h5)
        api_response = api_instance.get(id, integrate_scaler=integrate_scaler, model_type=model_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnModelApi->get: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnnModelApi* | [**get**](docs/AnnModelApi.md#get) | **GET** /api/ann/model/{id} | Download model file (*.h5)
*AnnModelApi* | [**get_metadata**](docs/AnnModelApi.md#get_metadata) | **GET** /api/ann/model/{id}/metadata | Get model metadata
*AnnModelApi* | [**head**](docs/AnnModelApi.md#head) | **HEAD** /api/ann/model/{id} | Check if h5 file exist
*AnnModelApi* | [**post**](docs/AnnModelApi.md#post) | **POST** /api/ann/model | Upload model(h5 file)
*AnnOptimizationApi* | [**get_status**](docs/AnnOptimizationApi.md#get_status) | **GET** /api/ann/{id}/status | Get status of optimization
*AnnOptimizationApi* | [**post**](docs/AnnOptimizationApi.md#post) | **POST** /api/ann | Starts new optimization using keras
*AnnOptimizationApi* | [**post_action**](docs/AnnOptimizationApi.md#post_action) | **POST** /api/ann/{id}/action/{optimizationAction} | Stop or cancel running optimization
*DataSetApi* | [**get**](docs/DataSetApi.md#get) | **GET** /api/dataset/{id} | Download dataset file (*.csv)
*DataSetApi* | [**head**](docs/DataSetApi.md#head) | **HEAD** /api/dataset/{id} | Check if dataset file exist
*DataSetApi* | [**post**](docs/DataSetApi.md#post) | **POST** /api/dataset | Upload dataset file (*.csv)
*PredictionApi* | [**post_array**](docs/PredictionApi.md#post_array) | **POST** /api/prediction/keras/array | Predict values from array
*PredictionApi* | [**post_file**](docs/PredictionApi.md#post_file) | **POST** /api/prediction/keras/file | 
*RandomForestModelApi* | [**get**](docs/RandomForestModelApi.md#get) | **GET** /api/random-forest/model/{id} | Download model file (*.h5)
*RandomForestModelApi* | [**get_metadata**](docs/RandomForestModelApi.md#get_metadata) | **GET** /api/random-forest/model/{id}/metadata | Get model metadata
*RandomForestModelApi* | [**head**](docs/RandomForestModelApi.md#head) | **HEAD** /api/random-forest/model/{id} | Check if h5 file exist
*RandomForestModelApi* | [**post**](docs/RandomForestModelApi.md#post) | **POST** /api/random-forest/model | Upload model(h5 file)
*RandomForestOptimizationApi* | [**get_status**](docs/RandomForestOptimizationApi.md#get_status) | **GET** /api/random-forest/{id}/status | Get status of optimization
*RandomForestOptimizationApi* | [**post**](docs/RandomForestOptimizationApi.md#post) | **POST** /api/random-forest | Starts new optimization using random forest
*RandomForestOptimizationApi* | [**post_action**](docs/RandomForestOptimizationApi.md#post_action) | **POST** /api/random-forest/{id}/action/{optimizationAction} | Stop or cancel running optimization
*RnnModelApi* | [**get**](docs/RnnModelApi.md#get) | **GET** /api/rnn/model/{id} | Download model file (*.h5)
*RnnModelApi* | [**get_metadata**](docs/RnnModelApi.md#get_metadata) | **GET** /api/rnn/model/{id}/metadata | Get model metadata
*RnnModelApi* | [**head**](docs/RnnModelApi.md#head) | **HEAD** /api/rnn/model/{id} | Check if h5 file exist
*RnnModelApi* | [**post**](docs/RnnModelApi.md#post) | **POST** /api/rnn/model | Upload model(h5 file)
*RnnOptimizationApi* | [**get_status**](docs/RnnOptimizationApi.md#get_status) | **GET** /api/rnn/{id}/status | Get status of optimization
*RnnOptimizationApi* | [**post**](docs/RnnOptimizationApi.md#post) | **POST** /api/rnn | Starts new reccurent neural network optimization using keras
*RnnOptimizationApi* | [**post_action**](docs/RnnOptimizationApi.md#post_action) | **POST** /api/rnn/{id}/action/{optimizationAction} | Stop or cancel running optimization
*SeriesModelApi* | [**get**](docs/SeriesModelApi.md#get) | **GET** /api/series/model/{id} | Download model file (*.h5)
*SeriesModelApi* | [**get_metadata**](docs/SeriesModelApi.md#get_metadata) | **GET** /api/series/model/{id}/metadata | Get model metadata
*SeriesModelApi* | [**head**](docs/SeriesModelApi.md#head) | **HEAD** /api/series/model/{id} | Check if h5 file exist
*SeriesModelApi* | [**post**](docs/SeriesModelApi.md#post) | **POST** /api/series/model | Upload model(h5 file)
*SeriesOptimizationApi* | [**get_status**](docs/SeriesOptimizationApi.md#get_status) | **GET** /api/series/{id}/status | Get status of optimization
*SeriesOptimizationApi* | [**post**](docs/SeriesOptimizationApi.md#post) | **POST** /api/series | 
*SeriesOptimizationApi* | [**post_action**](docs/SeriesOptimizationApi.md#post_action) | **POST** /api/series/{id}/action/{optimizationAction} | Stop or cancel running optimization
*TrainingApi* | [**post**](docs/TrainingApi.md#post) | **POST** /api/training/keras | 
*TrainingApi* | [**post_series**](docs/TrainingApi.md#post_series) | **POST** /api/training/keras-series | 


## Documentation For Models

 - [AggregationType](docs/AggregationType.md)
 - [AnnActivationFunction](docs/AnnActivationFunction.md)
 - [AnnHiddenLayerConfig](docs/AnnHiddenLayerConfig.md)
 - [AnnLayerConfig](docs/AnnLayerConfig.md)
 - [AnnOptimizationConfig](docs/AnnOptimizationConfig.md)
 - [AnnOptimizationEngineConfig](docs/AnnOptimizationEngineConfig.md)
 - [AnnOptimizationStatus](docs/AnnOptimizationStatus.md)
 - [AnnOptimizedModel](docs/AnnOptimizedModel.md)
 - [AnnTrainingAlgorithm](docs/AnnTrainingAlgorithm.md)
 - [AnnTrainingConfig](docs/AnnTrainingConfig.md)
 - [ConvergencyCriterion](docs/ConvergencyCriterion.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineObject3](docs/InlineObject3.md)
 - [InlineObject4](docs/InlineObject4.md)
 - [InputConfig](docs/InputConfig.md)
 - [InputWindowConfig](docs/InputWindowConfig.md)
 - [InputWindowRangeConfig](docs/InputWindowRangeConfig.md)
 - [NeuralNetworkType](docs/NeuralNetworkType.md)
 - [OptimizationAction](docs/OptimizationAction.md)
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
 - [Range](docs/Range.md)
 - [RangeInt](docs/RangeInt.md)
 - [RnnHiddenLayerConfig](docs/RnnHiddenLayerConfig.md)
 - [RnnOptimizationConfig](docs/RnnOptimizationConfig.md)
 - [RnnOptimizationStatus](docs/RnnOptimizationStatus.md)
 - [RnnOptimizedModel](docs/RnnOptimizedModel.md)
 - [SeriesOptimizationConfig](docs/SeriesOptimizationConfig.md)
 - [SeriesTrainingConfig](docs/SeriesTrainingConfig.md)
 - [TrainedNetwork](docs/TrainedNetwork.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




