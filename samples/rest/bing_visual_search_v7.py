# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Python example showcasing the usage of Bing Visual Search API using REST calls"""

import json
from pprint import pprint

import dotenv
import requests


def visual_search_basic(
    subscription_key,
    auth_header_name="Ocp-Apim-Subscription-Key",
    image_path="./my_image.jpg",
    mkt="en-us",
):
    """Bing Visual Search Basic REST call

    This sample calls the Bing Visual Search API with a query image and
    retrieves data and several web pages of the exact image and/or similar images.

    Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-visual-search/overview

    Args:
        subscription_key (str): Azure subscription key of Bing Visual Search service
        auth_header_name (str): Name of the authorization header
        image_path (str): Path of the image used for search
        mkt (str): Market to search in
    """
    # Construct a request
    endpoint = "https://api.bing.microsoft.com/v7.0/images/visualsearch"
    # Image_name is the name of the image
    with open(image_path, "rb") as img:
        file = {"image": ("Image_name", img.read())}
    params = {"mkt": mkt}
    headers = {
        auth_header_name: subscription_key,
        "Content-Type": "multipart/form-data",
    }

    # Call the API
    try:
        response = requests.post(
            endpoint, headers=headers, params=params, files=file, timeout=10
        )
        response.raise_for_status()
        return response

    except Exception as ex:
        raise Exception(f"Encountered exception: {ex}") from ex


def main() -> None:
    """Main Function that sends an example request and pretty prints the response"""
    # Load the environment variables from .env file
    env = dotenv.dotenv_values()

    SUBSCRIPTION_KEY_ENV_VAR_NAME = "BING_SEARCH_V7_VISUAL_SEARCH_SUBSCRIPTION_KEY"

    # Add your Bing Visual Search V7 subscription key to your environment variables / .env file
    subscription_key = env.get(SUBSCRIPTION_KEY_ENV_VAR_NAME)
    if not subscription_key:
        raise (
            RuntimeError(
                f"Please define the {SUBSCRIPTION_KEY_ENV_VAR_NAME} environment variable"
            )
        )

    try:
        response = visual_search_basic(subscription_key)
        print("\nResponse Headers:\n")
        pprint(dict(response.headers))

        print("\nJSON Response:\n")
        print(json.dumps(response.json(), indent=4))

    except Exception as ex:
        print(f"Encountered exception: {ex}")


if __name__ == "__main__":
    main()
