from __future__ import print_function
import time
import stylelens_sdk
from stylelens_sdk.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_sdk.ProductApi()
# product = stylelens_sdk.Product() # Product | Product object that needs to be added to the db.



try:
    api_response = api_instance.get_products(product_id='5a13a939247c1a00017051ef')
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_products: %s\n" % e)