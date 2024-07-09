# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import os
from image_search_client import ImageSearchClient
from azure.core.credentials import AzureKeyCredential


SUBSCRIPTION_KEY = None
ENDPOINT = "https://api.bing.microsoft.com" + "/v7.0/"


search_term = "canadian rockies"

"""
This application will search images on the web with the Bing Image Search API and print out first image result.
"""
if SUBSCRIPTION_KEY:
    # create the image search client
    client = ImageSearchClient(AzureKeyCredential(SUBSCRIPTION_KEY))
    # send a search query to the Bing Image Search API
    image_results = client.images.search(query=search_term)
    print("Searching the web for images of: {}".format(search_term))

    # Image results
    if image_results.value:
        first_image_result = image_results.value[0]
        print("Total number of images returned: {}".format(len(image_results.value)))
        print("First image thumbnail url: {}".format(first_image_result.thumbnail_url))
        print("First image content url: {}".format(first_image_result.content_url))
    else:
        print("Couldn't find image results!")
