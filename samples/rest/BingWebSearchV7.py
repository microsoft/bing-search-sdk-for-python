#Copyright (c) Microsoft Corporation. All rights reserved.
#Licensed under the MIT License.

# -*- coding: utf-8 -*-

import json
import os
from pprint import pprint
import requests
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

'''
This sample makes a call to the Bing Web Search API with a query and returns relevant web search.
Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-web-search/overview
'''
AUTH_HEADER=os.environ.get('BING_SEARCH_V7_AUTHORIZATION_HEADER', 'Ocp-Apim-Subscription-Key')
API_KEY='BING_SEARCH_V7_WEB_SEARCH_SUBSCRIPTION_KEY'

# Add your Bing Search V7 subscription key and endpoint to your environment variables.
endpoint = os.environ.get('BING_SEARCH_V7_WEB_SEARCH_ENDPOINT', 'https://api.bing.microsoft.com/v7.0/search')
subscription_key = os.environ.get(API_KEY)
if subscription_key is None:
    raise(RuntimeError(f'Please define the {API_KEY} environment variable'))

# Query term(s) to search for.
query = 'Microsoft'

# Construct a request
mkt = 'en-US'
params = { 'q': query, 'mkt': mkt }
headers = { AUTH_HEADER: subscription_key }

# Call the API
try:
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()

    print('\nHeaders:\n')
    print(response.headers)

    print('\nJSON Response:\n')
    pprint(response.json())
except Exception as ex:
    raise ex
