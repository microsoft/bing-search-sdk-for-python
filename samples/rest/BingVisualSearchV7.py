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
This sample calls the Bing Visual Search API with a query image and retrieves data and several web pages of the exact image and/or similar images
Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-visual-search/overview
"""
AUTH_HEADER_NAME = 'Ocp-Apim-Subscription-Key'
SUBSCRIPTION_KEY_ENV_VAR_NAME = 'BING_SEARCH_V7_VISUAL_SEARCH_SUBSCRIPTION_KEY'

# Add your Bing Visual Search subscription key to your environment variables / .env file
subscription_key = os.environ.get(SUBSCRIPTION_KEY_ENV_VAR_NAME)
if subscription_key is None:
    raise (RuntimeError(
        f'Please define the {SUBSCRIPTION_KEY_ENV_VAR_NAME} environment variable'))

image_path = './my_image.jpg'

endpoint = 'https://api.bing.microsoft.com/v7.0/images/visualsearch'
headers = {AUTH_HEADER_NAME: subscription_key,
           'Content-Type': 'multipart/form-data'}

# Replace <image_name> with a desired name for the image
file = {'image': ('<image_name>', open(image_path, 'rb'))}

try:
    response = requests.post(endpoint, headers=headers, files=file, timeout=10)
    response.raise_for_status()

    print('\nResponse Headers:\n')
    pprint(dict(response.headers))

    print('\nJSON Response:\n')
    print(json.dumps(response.json(), indent=4))
except Exception as ex:
    raise ex
