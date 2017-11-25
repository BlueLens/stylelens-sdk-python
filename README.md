# stylelens-sdk
This is a API document for Stylens Service

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import stylelens_sdk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import stylelens_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import stylelens_sdk
from stylelens_sdk.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_sdk.FeedApi()
offset = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # 
    api_response = api_instance.get_feeds(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeedApi->get_feeds: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://api.stylelens.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FeedApi* | [**get_feeds**](docs/FeedApi.md#get_feeds) | **GET** /feeds | 
*ObjectApi* | [**get_objects_by_image_file**](docs/ObjectApi.md#get_objects_by_image_file) | **POST** /objects | Query to search objects and products
*ObjectApi* | [**get_objects_by_product_id**](docs/ObjectApi.md#get_objects_by_product_id) | **GET** /objects/products/{productId} | Query to search multiple objects
*ProductApi* | [**get_product_by_hostcode_and_product_no**](docs/ProductApi.md#get_product_by_hostcode_and_product_no) | **GET** /products/hosts/{hostCode}/products/{productNo} | Get Product by hostCode and productNo
*ProductApi* | [**get_product_by_id**](docs/ProductApi.md#get_product_by_id) | **GET** /products/{productId} | Find Product by ID
*ProductApi* | [**get_products**](docs/ProductApi.md#get_products) | **GET** /products | Get Products by productId
*ProductApi* | [**get_products_by_image_file**](docs/ProductApi.md#get_products_by_image_file) | **GET** /products/images | Query to search products
*ProductApi* | [**get_products_by_image_id_and_object_id**](docs/ProductApi.md#get_products_by_image_id_and_object_id) | **GET** /products/images/{imageId}/objects/{objectId} | Get Products by imageId and objectId


## Documentation For Models

 - [BoxArray](docs/BoxArray.md)
 - [BoxObject](docs/BoxObject.md)
 - [BoxesArray](docs/BoxesArray.md)
 - [GetFeedResponse](docs/GetFeedResponse.md)
 - [GetObjectsResponse](docs/GetObjectsResponse.md)
 - [GetObjectsResponseData](docs/GetObjectsResponseData.md)
 - [GetProductResponse](docs/GetProductResponse.md)
 - [GetProductsResponse](docs/GetProductsResponse.md)
 - [Product](docs/Product.md)
 - [ProductsArray](docs/ProductsArray.md)
 - [SearchImageResponse](docs/SearchImageResponse.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: HTTP header


## Author

master@bluehack.net

