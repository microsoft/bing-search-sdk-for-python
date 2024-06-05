# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

# -*- coding: utf-8 -*-

import json
import os
from pprint import pprint
import requests
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

'''
This sample makes a call to the Bing News Search API with a text query and returns relevant news webpages.
Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-news-search/overview
'''
AUTH_HEADER_NAME='Ocp-Apim-Subscription-Key'
SUBSCRIPTION_KEY_ENV_VAR_NAME='BING_SEARCH_V7_NEWS_SEARCH_SUBSCRIPTION_KEY'

# Add your Bing News Search V7 subscription key to your environment variables / .env file
subscription_key = os.environ.get(SUBSCRIPTION_KEY_ENV_VAR_NAME)
if subscription_key is None:
    raise(RuntimeError(f'Please define the {SUBSCRIPTION_KEY_ENV_VAR_NAME} environment variable'))

# Construct a request
endpoint = 'https://api.bing.microsoft.com/v7.0/news/search'
query = 'Microsoft'
mkt = 'en-US'
params = {'q': query, 'mkt': mkt}
headers = {AUTH_HEADER_NAME: subscription_key}

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
