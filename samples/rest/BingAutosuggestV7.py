#Copyright (c) Microsoft Corporation. All rights reserved.
#Licensed under the MIT License.

# -*- coding: utf-8 -*-

import json
import os
import requests
from pprint import pprint
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

'''
This sample uses the Bing Autosuggest API to check the spelling of query words and then suggests corrections.
Bing Spell Check API: https://docs.microsoft.com/en-us/bing/search-apis/bing-spell-check/overview
'''
AUTH_HEADER=os.environ.get('BING_SEARCH_V7_AUTHORIZATION_HEADER', 'Ocp-Apim-Subscription-Key')
API_KEY='BING_SEARCH_V7_AUTO_SUGGEST_SUBSCRIPTION_KEY'

# Add your Bing Autosuggest subscription key and endpoint to your environment variables.
endpoint = os.environ.get('BING_SEARCH_V7_AUTO_SUGGEST_ENDPOINT', 'https://api.bing.microsoft.com/v7.0/suggestions')
subscription_key = os.environ.get(API_KEY)
if subscription_key is None:
    raise(RuntimeError(f'Please define the {API_KEY} environment variable'))

# Construct the request
mkt = 'en-US'
query = 'sail'
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
