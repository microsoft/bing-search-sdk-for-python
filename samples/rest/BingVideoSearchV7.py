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
This sample makes a call to the Bing Video Search API with a topic query and returns relevant video with data.
Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-video-search/overview
'''

AUTH_HEADER=os.environ.get('BING_SEARCH_V7_AUTHORIZATION_HEADER', 'Ocp-Apim-Subscription-Key')
API_KEY='BING_SEARCH_V7_VIDEO_SEARCH_SUBSCRIPTION_KEY'

# Add your Bing Search V7 subscription key and endpoint to your environment variables.
endpoint = os.environ.get('BING_SEARCH_V7_VIDEO_SEARCH_ENDPOINT', 'https://api.bing.microsoft.com/v7.0/videos')
subscriptionKey = os.environ.get(API_KEY)
if subscriptionKey is None:
    raise(RuntimeError(f'Please define the {API_KEY} environment variable'))

# Search query
query = 'kentucky derby'

# Construct a request
headers = {
    'Content-Type': 'application/json',
    AUTH_HEADER: subscriptionKey
    }
params = { 'q': query }

# Call the API
try:
    response = requests.get(endpoint + '/search', headers=headers, params=params)
    response.raise_for_status()

    # Print results
    print('\nHeaders:\n')
    print(response.headers)

    print('\nJSON Response:\n')
    pprint(response.json())
except Exception as ex:
    raise ex
