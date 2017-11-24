from __future__ import print_function
import time
import stylelens_sdk
from stylelens_sdk.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = stylelens_sdk.ProductApi()
product = stylelens_sdk.Product() # Product | Product object that needs to be added to the db.



try:
    api_response = api_instance.get_products_by_image_id_and_object_id('5a17c59ecfefac96631abb5f', 1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->add_product_by_image_id_and_object_id: %s\n" % e)