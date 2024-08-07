# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Python example showcasing the usage of Bing Custom Search API using REST calls"""

import json
from pprint import pprint

import dotenv
import requests
from requests import HTTPError


def custom_search_basic(
    query,
    subscription_key,
    custom_config_id,
    auth_header_name="Ocp-Apim-Subscription-Key",
    mkt="en-us",
):
    """Bing Custom Search Basic REST call

    This sample uses the Bing Custom Search API to search for a query topic and
    get back user-controlled web page results.
    Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-custom-search/overview

    May throw HTTPError in case of invalid parameters or a server error.

    Args:
        subscription_key (str): Azure subscription key of Bing Custom Search service
        custom_config_id (str): Custom Configuation ID obtained from the portal
        auth_header_name (str): Name of the authorization header
        query (str): Query to search for
        mkt (str): Market to search in
    """
    # Construct a request
    endpoint = "https://api.bing.microsoft.com/v7.0/custom/search"
    params = {"q": query, "mkt": mkt, "customconfig": custom_config_id}
    headers = {auth_header_name: subscription_key}

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
    SUBSCRIPTION_KEY_ENV_VAR_NAME = "BING_SEARCH_V7_CUSTOM_SEARCH_SUBSCRIPTION_KEY"
    CUSTOM_CONFIG_ID_ENV_VAR_NAME = "BING_CUSTOM_SEARCH_CONFIG"

    # Add your Bing Custom Search V7 subscription key and Configutation ID to
    # your environment variables / .env file
    subscription_key = env.get(SUBSCRIPTION_KEY_ENV_VAR_NAME)
    if not subscription_key:
        raise (
            RuntimeError(
                f"Please define the {SUBSCRIPTION_KEY_ENV_VAR_NAME} environment variable"
            )
        )
    custom_config_id = env.get(CUSTOM_CONFIG_ID_ENV_VAR_NAME, "1")

    response = custom_search_basic("Microsoft", subscription_key, custom_config_id)
    print("\nResponse Headers:\n")
    pprint(dict(response.headers))

    print("\nJSON Response:\n")
    print(json.dumps(response.json(), indent=4))


if __name__ == "__main__":
    main()
