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
This sample uses the Bing Entity Search API to retreive information about a well-known entity
Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-entity-search/overview
"""
AUTH_HEADER_NAME = 'Ocp-Apim-Subscription-Key'
SUBSCRIPTION_KEY_ENV_VAR_NAME = 'BING_SEARCH_V7_ENTITY_SEARCH_SUBSCRIPTION_KEY'

# Add your Bing Entity Search subscription key to your environment variables / .env file
subscription_key = os.environ.get(SUBSCRIPTION_KEY_ENV_VAR_NAME)
if subscription_key is None:
    raise (RuntimeError(
        f'Please define the {SUBSCRIPTION_KEY_ENV_VAR_NAME} environment variable'))

# Entity you want information about
query = 'alija izetbegović'

endpoint = 'https://api.bing.microsoft.com/v7.0/entities'
mkt = 'en-US'
params = {'mkt': mkt, 'q': query}
headers = {AUTH_HEADER_NAME: subscription_key}

try:
    response = requests.get(endpoint, headers=headers,
                            params=params, timeout=10)
    response.raise_for_status()

    print('\nResponse Headers:\n')
    pprint(dict(response.headers))

    print('\nJSON Response:\n')
    print(json.dumps(response.json(), indent=4))
except Exception as ex:
    raise ex
