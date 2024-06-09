import json
import os
from pprint import pprint
import requests
import urllib.parse
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

'''
This sample uses the Bing Entity Search v7 to search for restaurants and return details about it.
Bing Entity Search API: https://docs.microsoft.com/en-us/bing/search-apis/bing-entity-search/overview
'''
AUTH_HEADER_NAME='Ocp-Apim-Subscription-Key'
SUBSCRIPTION_KEY_ENV_VAR_NAME='BING_SEARCH_V7_ENTITY_SEARCH_SUBSCRIPTION_KEY'

# Add your Bing Entity Search subscription key to your environment variables / .env file
subscription_key = os.environ.get(SUBSCRIPTION_KEY_ENV_VAR_NAME)
if subscription_key is None:
    raise(RuntimeError(f'Please define the {SUBSCRIPTION_KEY_ENV_VAR_NAME} environment variable'))

# Entity you want to find
query = 'alija izetbegović'

# Construct the request
endpoint = 'https://api.bing.microsoft.com/v7.0/entities'
mkt = 'en-US'
params = 'mkt=' + mkt + '&q=' + urllib.parse.quote(query)
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
