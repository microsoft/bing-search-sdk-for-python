# Download and install Python at https://www.python.org/ 
# Run the following in a command console window: pip3 install requests

import json 
import os
from pprint import pprint
import requests
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

'''
This sample uses the Bing Visual Search API with a local, query image and returns several web links
and data of the exact image and/or similar images.
Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-visual-search/overview
'''
AUTH_HEADER_NAME='Ocp-Apim-Subscription-Key'
SUBSCRIPTION_KEY_ENV_VAR_NAME='BING_SEARCH_V7_VISUAL_SEARCH_SUBSCRIPTION_KEY'

# Add your Bing Visual Search V7 subscription key to your environment variables / .env file
subscription_key = os.environ.get(SUBSCRIPTION_KEY_ENV_VAR_NAME)
if subscription_key is None:
    raise(RuntimeError(f'Please define the {SUBSCRIPTION_KEY_ENV_VAR_NAME} environment variable'))

image_path = './my_image.jpg'

# Construct the request
endpoint = 'https://api.bing.microsoft.com/v7.0/images/visualsearch'
headers = {AUTH_HEADER_NAME: subscription_key,
           'Content-Type': 'multipart/form-data' }

file = {'image' : ('Image_name', open(image_path, 'rb'))} # Image_name is the name of the image
    
# Call the API
try:
    response = requests.post(endpoint, headers=headers, files=file)
    response.raise_for_status()

    print('\nHeaders:\n')
    print(response.headers)

    print('\nJSON Response:\n')
    pprint(response.json())
except Exception as ex:
    raise ex
