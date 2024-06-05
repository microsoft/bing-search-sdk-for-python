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
AUTH_HEADER=os.environ.get('BING_SEARCH_V7_AUTHORIZATION_HEADER', 'Ocp-Apim-Subscription-Key')
API_KEY='BING_SEARCH_V7_VISUAL_SEARCH_SUBSCRIPTION_KEY'

# Add your Bing Search V7 subscription key and endpoint to your environment variables.
endpoint = os.environ.get('BING_SEARCH_V7_VISUAL_SEARCH_ENDPOINT', 'https://api.bing.microsoft.com/v7.0/images/visualsearch')
subscription_key = os.environ.get(API_KEY)
if subscription_key is None:
    raise(RuntimeError(f'Please define the {API_KEY} environment variable'))

image_path = './my_image.jpg'

# Construct the request
headers = {AUTH_HEADER: subscription_key}
file = {'image' : ('MY-IMAGE', open(image_path, 'rb'))} # MY-IMAGE is the name of the image file (no extention)
    
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
