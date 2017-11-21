# stylelens_sdk.ProductApi

All URIs are relative to *http://api.stylelens.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_products**](ProductApi.md#get_products) | **POST** /products | Query to search products


# **get_products**
> GetProductsResponse get_products(file=file)

Query to search products



### Example 
```python
from __future__ import print_function
import time
import stylelens_sdk
from stylelens_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = stylelens_sdk.ProductApi()
file = '/path/to/file.txt' # file | Image file to upload (only support jpg format yet) (optional)

try: 
    # Query to search products
    api_response = api_instance.get_products(file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| Image file to upload (only support jpg format yet) | [optional] 

### Return type

[**GetProductsResponse**](GetProductsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

