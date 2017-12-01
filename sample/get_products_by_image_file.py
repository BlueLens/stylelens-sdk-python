from __future__ import print_function
import time
import stylelens_sdk
from stylelens_sdk.rest import ApiException
from stylelens_sdk.models.get_objects_response import GetObjectsResponse
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_sdk.ProductApi()

file = '/Users/bok95/Downloads/1.jpg'


try:
    api_response = api_instance.get_products_by_image_file(file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_products_by_image_fil: %s\n" % e)