# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Python example showcasing the usage of Bing Image Search API using REST calls"""

import json
from pprint import pprint

import dotenv
import requests


def image_search_basic(
    query,
    subscription_key,
    auth_header_name="Ocp-Apim-Subscription-Key",
    mkt="en-us",
):
    """Bing Image Search Basic REST call

    This sample makes a call to the Bing Image Search API with a text query and
    returns relevant images with data.
    Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-image-search/overview

    Args:
        subscription_key (str): Azure subscription key of Bing Image Search service
        auth_header_name (str): Name of the authorization header
        query (str): Query to search for
        mkt (str): Market to search in
    """
    # Construct a request
    endpoint = "https://api.bing.microsoft.com/v7.0/images/search"
    params = {"q": query, "mkt": mkt}
    headers = {auth_header_name: subscription_key}

    # Call the API
    try:
        response = requests.get(endpoint, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        return response

    except Exception as ex:
        raise Exception(f"Encountered exception: {ex}") from ex


def main() -> None:
    """Main Function that sends an example request and pretty prints the response"""
    # Load the environment variables from .env file
    env = dotenv.dotenv_values()

    SUBSCRIPTION_KEY_ENV_VAR_NAME = "BING_SEARCH_V7_IMAGE_SEARCH_SUBSCRIPTION_KEY"

    # Add your Bing Image Search V7 subscription key to your environment variables / .env file
    subscription_key = env.get(SUBSCRIPTION_KEY_ENV_VAR_NAME)
    if not subscription_key:
        raise (
            RuntimeError(
                f"Please define the {SUBSCRIPTION_KEY_ENV_VAR_NAME} environment variable"
            )
        )

    try:
        response = image_search_basic("Arabian horse", subscription_key)
        print("\nResponse Headers:\n")
        pprint(dict(response.headers))

        print("\nJSON Response:\n")
        print(json.dumps(response.json(), indent=4))

    except Exception as ex:
        print(f"Encountered exception: {ex}")


if __name__ == "__main__":
    main()