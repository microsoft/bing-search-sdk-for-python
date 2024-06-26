# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Python example showcasing the usage of Bing Spell Check API using REST calls"""

import json
from pprint import pprint

import dotenv
import requests
from requests import HTTPError


def spell_check_basic(
    query,
    subscription_key,
    auth_header_name="Ocp-Apim-Subscription-Key",
    mkt="en-us",
    mode="proof",
):
    """Bing Spell Check Basic REST call

    This sample uses the Bing Spell Check API to perform contextual grammar and spell
        checking on a text string and then suggests corrections with a scored confidence
    Bing Spell Check API:
    Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-spell-check/overview

    May throw HTTPError in case of invalid parameters or a server error.

    Args:
        subscription_key (str): Azure subscription key of Bing Spell Check service
        auth_header_name (str): Name of the authorization header
        query (str): Query to spell check
        mkt (str): Market code to deduce language and locale
        mode (str): 'spell' or 'proof'
    """
    # Construct a request
    endpoint = "https://api.bing.microsoft.com/v7.0/spellcheck"
    headers = {
        auth_header_name: subscription_key,
        "Content-Type": "application/x-www-form-urlencoded",
    }

    # Call the API
    try:
        response = requests.post(
            endpoint,
            headers=headers,
            params={"mkt": mkt, "mode": mode},
            data={"text": query},
            timeout=10,
        )
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
    SUBSCRIPTION_KEY_ENV_VAR_NAME = "BING_SEARCH_V7_SPELL_CHECK_SUBSCRIPTION_KEY"

    # Add your Bing Spell Check V7 subscription key to your environment variables / .env file
    subscription_key = env.get(SUBSCRIPTION_KEY_ENV_VAR_NAME)
    if not subscription_key:
        raise (
            RuntimeError(
                f"Please define the {SUBSCRIPTION_KEY_ENV_VAR_NAME} environment variable"
            )
        )

    response = spell_check_basic(
        "when i went two the houze i heared they'r'e voice and they're srcreams.\
    I walk their and told: \"helo fren\"",
        subscription_key,
    )
    print("\nResponse Headers:\n")
    pprint(dict(response.headers))

    print("\nJSON Response:\n")
    print(json.dumps(response.json(), indent=4))


if __name__ == "__main__":
    main()
