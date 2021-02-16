# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import json
import os
from pprint import pprint
import requests
import urllib.parse

'''
This sample uses the Bing Spell Check API to check the spelling of query words 
and then suggests corrections with a scored confidence.
Bing Spell Check API: https://docs.microsoft.com/en-us/bing/search-apis/bing-spell-check/overview
'''

# Add your Bing Spell Check subscription key and endpoint to your environment variables.
key = os.environ['BING_SPELL_CHECK_SUBSCRIPTION_KEY']
endpoint = os.environ['BING_SPELL_CHECK_ENDPOINT'] + '/bing/v7.0/spellcheck'

# Query you want spell-checked. 
query = 'Hollo, wrld!'

# Construct request
params = urllib.parse.urlencode( { 'mkt': 'en-US', 'mode': 'proof', 'text': query } )
headers = { 'Ocp-Apim-Subscription-Key': key,
            'Content-Type': 'application/x-www-form-urlencoded' }

# Optional headers
#
# X-MSEdge-ClientIP: 999.999.999.999  
# X-Search-Location: lat: +90.0000000000000;long: 00.0000000000000;re:100.000000000000
# X-MSEdge-ClientID: <Client ID from Previous Response Goes Here>

# Call the API
try:
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()

    print("\nHeaders:\n")
    print(response.headers)

    print("\nJSON Response:\n")
    pprint(response.json())
except Exception as ex:
    raise ex