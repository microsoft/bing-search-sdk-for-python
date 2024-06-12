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
This sample uses the Bing Spell Check API to perform contextual grammar and spell checking on a text string and then suggests corrections with a scored confidence
Bing Spell Check API: https://docs.microsoft.com/en-us/bing/search-apis/bing-spell-check/overview
"""
AUTH_HEADER_NAME = 'Ocp-Apim-Subscription-Key'
SUBSCRIPTION_KEY_ENV_VAR_NAME = 'BING_SEARCH_V7_SPELL_CHECK_SUBSCRIPTION_KEY'

# Add your Bing Spell Check subscription key to your environment variables / .env file
subscription_key = os.environ.get(SUBSCRIPTION_KEY_ENV_VAR_NAME)
if subscription_key is None:
    raise (RuntimeError(
        f'Please define the {SUBSCRIPTION_KEY_ENV_VAR_NAME} environment variable'))

# Query you want spell-checked
query = 'when i went two the houze i heared they\'r\'e voice and they\'re srcreams. I walk their and told: "helo fren"'

endpoint = 'https://api.bing.microsoft.com/v7.0/spellcheck'
params = {'mkt': 'en-US', 'mode': 'proof', 'text': query}
headers = {AUTH_HEADER_NAME: subscription_key,
           'Content-Type': 'application/x-www-form-urlencoded'}

try:
    response = requests.post(endpoint, headers=headers,
                             params=params, timeout=10)
    response.raise_for_status()

    print('\nResponse Headers:\n')
    pprint(dict(response.headers))

    print('\nJSON Response:\n')
    print(json.dumps(response.json(), indent=4))
except Exception as ex:
    raise ex
