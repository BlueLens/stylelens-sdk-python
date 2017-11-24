# stylelens_sdk.FeedApi

All URIs are relative to *http://api.stylelens.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_feeds**](FeedApi.md#get_feeds) | **GET** /feeds | 


# **get_feeds**
> GetFeedResponse get_feeds(offset=offset, limit=limit)



Returns Main Feeds

### Example 
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**GetFeedResponse**](GetFeedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

