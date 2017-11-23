from __future__ import print_function
import time
import stylelens_sdk
from stylelens_sdk.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_sdk.ProductApi()
product = stylelens_sdk.Product() # Product | Product object that needs to be added to the db.



try:
    # Added a new Product
    api_response = api_instance.get_product_by_hostcode_and_product_no('HC0002', '949')
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->add_product_by_hostcode_and_product_no: %s\n" % e)