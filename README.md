# blackfox-restapi

- API version: v1
- Package version: 1.0.0

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/vodena/BlackFoxRestApiPython.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/vodena/BlackFoxRestApiPython.git`)

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

# create an instance of the API class
api_instance = blackfox_restapi.DataSetApi(blackfox_restapi.ApiClient(configuration))
id = 'id_example' # str | Dataset Id

try:
    # Download dataset file (*.csv)
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSetApi->get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DataSetApi* | [**get**](docs/DataSetApi.md#get) | **GET** /api/dataset/{id} | Download dataset file (*.csv)
*DataSetApi* | [**head**](docs/DataSetApi.md#head) | **HEAD** /api/dataset/{id} | Check if dataset file exist
*DataSetApi* | [**post**](docs/DataSetApi.md#post) | **POST** /api/dataset | Upload dataset file (*.csv)
*NetworkApi* | [**get**](docs/NetworkApi.md#get) | **GET** /api/network/{id} | Download model file (*.h5)
*NetworkApi* | [**get_metadata**](docs/NetworkApi.md#get_metadata) | **GET** /api/network/{id}/metadata | Get model metadata
*NetworkApi* | [**head**](docs/NetworkApi.md#head) | **HEAD** /api/network/{id} | Check if h5 file exist
*NetworkApi* | [**post**](docs/NetworkApi.md#post) | **POST** /api/network | Upload model(h5 file)
*OptimizationApi* | [**get_status**](docs/OptimizationApi.md#get_status) | **GET** /api/optimization/keras/{id}/status | Get status of optimization
*OptimizationApi* | [**post**](docs/OptimizationApi.md#post) | **POST** /api/optimization/keras | Starts new optimization using keras
*OptimizationApi* | [**post_action**](docs/OptimizationApi.md#post_action) | **POST** /api/optimization/keras/{id}/action/{optimizationAction} | Stop or cancel running optimization
*OptimizationApi* | [**post_series**](docs/OptimizationApi.md#post_series) | **POST** /api/optimization/keras-series | Starts new series optimization using keras
*PredictionApi* | [**post_array**](docs/PredictionApi.md#post_array) | **POST** /api/prediction/keras/array | Predict values from array
*PredictionApi* | [**post_file**](docs/PredictionApi.md#post_file) | **POST** /api/prediction/keras/file | 
*RecurrentOptimizationApi* | [**get_status**](docs/RecurrentOptimizationApi.md#get_status) | **GET** /api/optimization/rnn/keras/{id}/status | Get status of optimization
*RecurrentOptimizationApi* | [**post**](docs/RecurrentOptimizationApi.md#post) | **POST** /api/optimization/rnn/keras | Starts new reccurent neural network optimization using keras
*RecurrentOptimizationApi* | [**post_action**](docs/RecurrentOptimizationApi.md#post_action) | **POST** /api/optimization/rnn/keras/{id}/action/{optimizationAction} | Stop or cancel running optimization
*TrainingApi* | [**post**](docs/TrainingApi.md#post) | **POST** /api/training/keras | 
*TrainingApi* | [**post_series**](docs/TrainingApi.md#post_series) | **POST** /api/training/keras-series | 


## Documentation For Models

 - [ConvergencyCriterion](docs/ConvergencyCriterion.md)
 - [InputConfig](docs/InputConfig.md)
 - [InputWindowConfig](docs/InputWindowConfig.md)
 - [InputWindowRangeConfig](docs/InputWindowRangeConfig.md)
 - [KerasHiddenLayerConfig](docs/KerasHiddenLayerConfig.md)
 - [KerasLayerConfig](docs/KerasLayerConfig.md)
 - [KerasOptimizationConfig](docs/KerasOptimizationConfig.md)
 - [KerasOptimizationStatus](docs/KerasOptimizationStatus.md)
 - [KerasOptimizedNetwork](docs/KerasOptimizedNetwork.md)
 - [KerasRecurrentHiddenLayerConfig](docs/KerasRecurrentHiddenLayerConfig.md)
 - [KerasRecurrentOptimizationConfig](docs/KerasRecurrentOptimizationConfig.md)
 - [KerasRecurrentOptimizationStatus](docs/KerasRecurrentOptimizationStatus.md)
 - [KerasRecurrentOptimizedNetwork](docs/KerasRecurrentOptimizedNetwork.md)
 - [KerasSeriesOptimizationConfig](docs/KerasSeriesOptimizationConfig.md)
 - [KerasSeriesTrainingConfig](docs/KerasSeriesTrainingConfig.md)
 - [KerasTrainingConfig](docs/KerasTrainingConfig.md)
 - [OptimizationEngineConfig](docs/OptimizationEngineConfig.md)
 - [OutputWindowConfig](docs/OutputWindowConfig.md)
 - [PredictionArrayConfig](docs/PredictionArrayConfig.md)
 - [PredictionFileConfig](docs/PredictionFileConfig.md)
 - [Range](docs/Range.md)
 - [RecurrentOptimizationEngineConfig](docs/RecurrentOptimizationEngineConfig.md)
 - [TrainedNetwork](docs/TrainedNetwork.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



