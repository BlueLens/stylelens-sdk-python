# stylelens_sdk.ObjectApi

All URIs are relative to *http://api.stylelens.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_objects**](ObjectApi.md#get_objects) | **POST** /objects | Query to search multiple objects
[**get_objects_by_product_id**](ObjectApi.md#get_objects_by_product_id) | **GET** /objects/products/{productId} | Query to search multiple objects


# **get_objects**
> GetObjectsResponse get_objects(file=file)

Query to search multiple objects



### Example 
```python
from __future__ import print_function
import time
import stylelens_sdk
from stylelens_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = stylelens_sdk.ObjectApi()
file = '/path/to/file.txt' # file | Image file to upload (only support jpg format yet) (optional)

try: 
    # Query to search multiple objects
    api_response = api_instance.get_objects(file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectApi->get_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| Image file to upload (only support jpg format yet) | [optional] 

### Return type

[**GetObjectsResponse**](GetObjectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_objects_by_product_id**
> GetObjectsResponse get_objects_by_product_id(product_id)

Query to search multiple objects



### Example 
```python
from __future__ import print_function
import time
import stylelens_sdk
from stylelens_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = stylelens_sdk.ObjectApi()
product_id = 'product_id_example' # str | 

try: 
    # Query to search multiple objects
    api_response = api_instance.get_objects_by_product_id(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectApi->get_objects_by_product_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  | 

### Return type

[**GetObjectsResponse**](GetObjectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

