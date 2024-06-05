# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

# You may need the below as well
# pip install pipenv
# pipenv install requests
# <importsAndVars>
import json
import os
from pprint import pprint
import requests 
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

'''
This sample uses the Bing Custom Search API to search for a query topic and get back user-controlled web page results.
Bing Custom Search API: https://docs.microsoft.com/en-us/bing/search-apis/bing-custom-search/overview 
'''
AUTH_HEADER=os.environ.get('BING_SEARCH_V7_AUTHORIZATION_HEADER', 'Ocp-Apim-Subscription-Key')
API_KEY='BING_SEARCH_V7_CUSTOM_SEARCH_SUBSCRIPTION_KEY'

# Add your Bing Custom Search subscription key and endpoint to your environment variables.
subscriptionKey = os.environ.get(API_KEY)
endpoint = os.environ.get('BING_SEARCH_V7_CUSTOM_SEARCH_ENDPOINT', 'https://api.bing.microsoft.com/v7.0/custom')
customConfigId = os.environ.get('BING_CUSTOM_SEARCH_CONFIG', '1')
if subscriptionKey is None:
    raise(RuntimeError(f'Please define the {API_KEY} environment variable'))

searchTerm = 'Microsoft'
# </importsAndVars>
# <url>
# Add your Bing Custom Search endpoint to your environment variables.
url = endpoint + '/search?q=' + searchTerm + '&customconfig=' + customConfigId
# </url>
# <request>
r = requests.get(url, headers={AUTH_HEADER: subscriptionKey})
pprint(json.loads(r.text))
# </request>
