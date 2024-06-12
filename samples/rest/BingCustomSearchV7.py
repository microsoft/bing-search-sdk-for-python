# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License
import json
import os
from pprint import pprint

import requests
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

"""
This sample uses the Bing Custom Search API to search for a query topic and get back user-controlled web page results
Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-custom-search/overview 
"""
AUTH_HEADER_NAME = 'Ocp-Apim-Subscription-Key'
SUBSCRIPTION_KEY_ENV_VAR_NAME = 'BING_SEARCH_V7_CUSTOM_SEARCH_SUBSCRIPTION_KEY'

# Add your Bing Custom Search subscription key to your environment variables / .env file
subscription_key = os.environ.get(SUBSCRIPTION_KEY_ENV_VAR_NAME)
customConfigId = os.environ.get('BING_CUSTOM_SEARCH_CONFIG', '1')
if subscription_key is None:
    raise (RuntimeError(
        f'Please define the {SUBSCRIPTION_KEY_ENV_VAR_NAME} environment variable'))

searchTerm = 'Microsoft'
params = {'q': searchTerm, 'customconfig': customConfigId}


url = 'https://api.bing.microsoft.com/v7.0/custom/search'

response = requests.get(
    url, headers={AUTH_HEADER_NAME: subscription_key}, params=params, timeout=10)
print('\nResponse Headers:\n')
pprint(dict(response.headers))

print('\nJSON Response:\n')
print(json.dumps(response.json(), indent=4))
