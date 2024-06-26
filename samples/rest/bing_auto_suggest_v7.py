# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Python example showcasing the usage of Bing Auto Suggest API using REST calls"""

import json
from pprint import pprint

import dotenv
import requests
from requests import HTTPError


def auto_suggest_basic(
    query, subscription_key, auth_header_name="Ocp-Apim-Subscription-Key", mkt="en-us"
):
    """Bing Auto Suggest Basic REST call

    This sample uses the Bing Autosuggest API to provide a list of suggested search query strings
    Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-autosuggest/overview

    May throw HTTPError in case of invalid parameters or a server error.

    Args:
        subscription_key (str): Azure subscription key of Bing Auto Suggest service
        auth_header_name (str): Name of the authorization header
        query (str): Query to get suggestions for
        mkt (str): Market to search in
    """

    # Construct the request
    endpoint = "https://api.bing.microsoft.com/v7.0/suggestions"
    params = {"q": query, "mkt": mkt}
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
    SUBSCRIPTION_KEY_ENV_VAR_NAME = "BING_SEARCH_V7_AUTO_SUGGEST_SUBSCRIPTION_KEY"

    # Add your Bing Auto Suggest V7 subscription key to your environment variables / .env file
    subscription_key = env.get(SUBSCRIPTION_KEY_ENV_VAR_NAME)
    if not subscription_key:
        raise (
            RuntimeError(
                f"Please define the {SUBSCRIPTION_KEY_ENV_VAR_NAME} environment variable"
            )
        )

    response = auto_suggest_basic(query="sail", subscription_key=subscription_key)
    print("\nResponse Headers:\n")
    pprint(dict(response.headers))

    print("\nJSON Response:\n")
    print(json.dumps(response.json(), indent=4))


if __name__ == "__main__":
    main()
