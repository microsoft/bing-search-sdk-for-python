# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Python example showcasing the usage of Bing Visual Search API using REST calls"""

import json
from pprint import pprint

import dotenv
import requests
from requests import HTTPError


def visual_search_basic(
    subscription_key,
    image_url=None,
    image_path=None,
    auth_header_name="Ocp-Apim-Subscription-Key",
    mkt="en-us",
):
    """Bing Visual Search Basic REST call

    This sample calls the Bing Visual Search API with a query image and
    retrieves data and several web pages of the exact image and/or similar images.

    Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-visual-search/overview

    May throw HTTPError in case of invalid parameters or a server error.

    Args:
        subscription_key (str): Azure subscription key of Bing Visual Search service
        auth_header_name (str): Name of the authorization header
        image_url (str): Url of the image used for search
        image_path (str): Path of the image used for search
        mkt (str): Market to search in
    """
    # Default value for demo purposes
    image_url = (
        image_url
        or "https://upload.wikimedia.org/wikipedia/commons/4/40/Bing_Cherries_(USDA_ARS).jpg"
    )

    # Construct a request
    endpoint = "https://api.bing.microsoft.com/v7.0/images/visualsearch"
    params = {"mkt": mkt}
    headers = {
        auth_header_name: subscription_key,
        "Content-Type": "multipart/form-data",
    }

    # Call the API
    try:
        if image_path:
            # Image_name is the name of the image
            with open(image_path, "rb") as img:
                file = {"image": ("Image_name", img.read())}
            response = requests.post(
                endpoint, headers=headers, params=params, files=file, timeout=10
            )

        else:
            headers["Content-Type"] += ";boundary=--example-boundary-1234"
            body = (
                "--example-boundary-1234\n"
                'Content-Disposition: form-data; name="knowledgeRequest"\n\n'
                '{"imageInfo": {"url": "' + image_url + '"}\n}\n'
                "--example-boundary-1234--"
            )
            response = requests.post(
                endpoint, headers=headers, params=params, data=body, timeout=10
            )

        response.raise_for_status()
        return response
    except HTTPError as ex:
        print(ex)
        print("++The above exception was thrown and handled succesfully++")
        return response
    except FileNotFoundError as ex:
        print(ex)
        print("++The above exception was thrown and handled succesfully++")
        return


def main() -> None:
    """Main Function that sends an example request and pretty prints the response"""
    # Load the environment variables from .env file
    env = dotenv.dotenv_values()

    # pylint: disable=invalid-name
    SUBSCRIPTION_KEY_ENV_VAR_NAME = "BING_SEARCH_V7_VISUAL_SEARCH_SUBSCRIPTION_KEY"

    # Add your Bing Visual Search V7 subscription key to your environment variables / .env file
    subscription_key = env.get(SUBSCRIPTION_KEY_ENV_VAR_NAME)
    if not subscription_key:
        raise (
            RuntimeError(
                f"Please define the {SUBSCRIPTION_KEY_ENV_VAR_NAME} environment variable"
            )
        )

    response = visual_search_basic(
        subscription_key,
        # image_path="./my_image.jpg",
        # image_url="https://upload.wikimedia.org/wikipedia/commons/4/40/Bing_Cherries_(USDA_ARS).jpg",
    )
    pprint(dict(response.headers))

    print("\nJSON Response:\n")
    print(json.dumps(response.json(), indent=4))


if __name__ == "__main__":
    main()
