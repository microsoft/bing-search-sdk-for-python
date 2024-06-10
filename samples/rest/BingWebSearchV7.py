import json
import os
from pprint import pprint
import requests
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

"""
This sample makes a call to the Bing Web Search API with a text query and returns relevant web pages
Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-web-search/overview
"""
AUTH_HEADER_NAME = 'Ocp-Apim-Subscription-Key'
SUBSCRIPTION_KEY_ENV_VAR_NAME = 'BING_SEARCH_V7_WEB_SEARCH_SUBSCRIPTION_KEY'

# Add your Bing Web Search V7 subscription key to your environment variables / .env file
subscription_key = os.environ.get(SUBSCRIPTION_KEY_ENV_VAR_NAME)
if subscription_key is None:
    raise (RuntimeError(
        f'Please define the {SUBSCRIPTION_KEY_ENV_VAR_NAME} environment variable'))

# Query term(s) to search for.
query = 'Microsoft'

# Construct a request
endpoint = 'https://api.bing.microsoft.com/v7.0/search'
mkt = 'en-US'
params = {'q': query, 'mkt': mkt}
headers = {AUTH_HEADER_NAME: subscription_key}

# Call the API
try:
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()

    print('\nResponse Headers:\n')
    pprint(dict(response.headers))

    print('\nJSON Response:\n')
    print(json.dumps(response.json(), indent=4))
except Exception as ex:
    raise ex
