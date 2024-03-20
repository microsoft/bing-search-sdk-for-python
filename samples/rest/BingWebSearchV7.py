#Copyright (c) Microsoft Corporation. All rights reserved.
#Licensed under the MIT License.

# -*- coding: utf-8 -*-

import json
import os
from pprint import pprint
import requests

'''
This sample makes a call to the Bing Web Search API with a query and returns relevant web search.
Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-web-search/overview
'''

# Add your Bing Search V7 subscription key and endpoint to your environment variables.
subscription_key = os.environ['84900ec94e08423b9468f053da33eff9']
endpoint = os.environ['https://api.bing.microsoft.com/'] + "/v7.0/search"

# Query images to search for.
image_path = 'MY-IMAGE' # for example: my_image.jpg

# Construct the request
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
file = {'image' : ('MY-IMAGE', open(image_path, 'rb'))} # MY-IMAGE is the name of the image file (no extention)
    
# Call the API
try:
    response = requests.post(endpoint, headers=headers, files=file)
    response.raise_for_status()

    print("\nHeaders:\n")
    print(response.headers)

    print("\nJSON Response:\n")
    pprint(response.json())
except Exception as ex:
    raise ex
