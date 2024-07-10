# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Python example showcasing the usage of Bing Video Search API using REST calls"""

import json
from pprint import pprint

import dotenv
import requests
from requests import HTTPError


def video_search_basic(
    query, subscription_key, auth_header_name="Ocp-Apim-Subscription-Key", mkt="en-us"
):
    """Bing Video Search Basic REST call

    This sample makes a call to the Bing Video Search API with a topic query and
    returns relevant video with data.

    Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-video-search/overview

    May throw HTTPError in case of invalid parameters or a server error.

    Args:
        subscription_key (str): Azure subscription key of Bing Video Search service
        auth_header_name (str): Name of the authorization header
        query (str): Query to search for
        mkt (str): Market to search in
    """
    # Construct a request
    endpoint = "https://api.bing.microsoft.com/v7.0/videos/search"
    params = {"q": query, "mkt": mkt}
    headers = {auth_header_name: subscription_key, "Content-Type": "application/json"}

    # Call the API
    try:
        response = requests.get(endpoint, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        return response
    except HTTPError as ex:
        print(ex)
        print("++The above exception was thrown and handled succesfully++")
        return response


def main() -> None:
    """Main Function that sends an example request and pretty prints the response"""
    # Load the environment variables from .env file
    env = dotenv.dotenv_values()

    # pylint: disable=invalid-name
    SUBSCRIPTION_KEY_ENV_VAR_NAME = "BING_SEARCH_V7_VIDEO_SEARCH_SUBSCRIPTION_KEY"

    # Add your Bing Video Search V7 subscription key to your environment variables / .env file
    subscription_key = env.get(SUBSCRIPTION_KEY_ENV_VAR_NAME)
    if not subscription_key:
        raise (
            RuntimeError(
                f"Please define the {SUBSCRIPTION_KEY_ENV_VAR_NAME} environment variable"
            )
        )

    response = video_search_basic("kentucky derby", subscription_key)
    print("\nResponse Headers:\n")
    pprint(dict(response.headers))

    print("\nJSON Response:\n")
    print(json.dumps(response.json(), indent=4))


if __name__ == "__main__":
    main()
