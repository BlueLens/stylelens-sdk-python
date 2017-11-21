from __future__ import print_function
import time
import stylelens_sdk
from stylelens_sdk.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_sdk.ProductApi()
# product = stylelens_sdk.Product() # Product | Product object that needs to be added to the db.

file = '/Users/bok95/Desktop/img.jpg'


try:
    api_response = api_instance.get_products(file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_products: %s\n" % e)