# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import os
from web_search_client import WebSearchClient
from web_search_client.models import SafeSearch
from azure.core.credentials import AzureKeyCredential
import dotenv

ENDPOINT = "https://api.bing.microsoft.com"+  "/v7.0/"




def result_types_lookup(subscription_key):
    """WebSearchResultTypesLookup.

    This will look up a single query (Xbox) and print out name and url for first web, image, news and videos results.
    """
    client = WebSearchClient(AzureKeyCredential(subscription_key))

    try:

        web_data = client.web.search(query="xbox")
        print('Searched for Query# " Xbox "')

        # WebPages
        if web_data.web_pages.value:

            print("Webpage Results#{}".format(len(web_data.web_pages.value)))

            first_web_page = web_data.web_pages.value[0]
            print("First web page name: {} ".format(first_web_page.name))
            print("First web page URL: {} ".format(first_web_page.url))

        else:
            print("Didn't see any Web data..")

        # Images
        if web_data.images.value:

            print("Image Results#{}".format(len(web_data.images.value)))

            first_image = web_data.images.value[0]
            print("First Image name: {} ".format(first_image.name))
            print("First Image URL: {} ".format(first_image.url))

        else:
            print("Didn't see any Image..")

        # News
        if web_data.news.value:

            print("News Results#{}".format(len(web_data.news.value)))

            first_news = web_data.news.value[0]
            print("First News name: {} ".format(first_news.name))
            print("First News URL: {} ".format(first_news.url))

        else:
            print("Didn't see any News..")

        # Videos
        if web_data.videos.value:

            print("Videos Results#{}".format(len(web_data.videos.value)))

            first_video = web_data.videos.value[0]
            print("First Videos name: {} ".format(first_video.name))
            print("First Videos URL: {} ".format(first_video.url))

        else:
            print("Didn't see any Videos..")

    except Exception as err:
        print("Encountered exception. {}".format(err))


def web_results_with_count_and_offset(subscription_key):
    """WebResultsWithCountAndOffset.

    This will search (Best restaurants in Seattle), verify number of results and print out name and url of first result.
    """

    client = WebSearchClient(AzureKeyCredential(subscription_key))

    try:
        web_data = client.web.search(
            query="Best restaurants in Seattle", offset=10, count=20
        )
        print('Searched for Query# " Best restaurants in Seattle "')

        if web_data.web_pages.value:

            print("Webpage Results#{}".format(len(web_data.web_pages.value)))

            first_web_page = web_data.web_pages.value[0]
            print("First web page name: {} ".format(first_web_page.name))
            print("First web page URL: {} ".format(first_web_page.url))

        else:
            print("Didn't see any Web data..")

    except Exception as err:
        print("Encountered exception. {}".format(err))


def web_search_with_response_filter(subscription_key):
    """WebSearchWithResponseFilter.

    This will search (Microsoft) with response filters to news and print details of news.
    """

    client = WebSearchClient(AzureKeyCredential(subscription_key))

    try:
        web_data = client.web.search(query="Microsoft", response_filter=["News"])
        print('Searched for Query# " Microsoft " with response filters "News"')

        # News attribute since I filtered "News"
        if web_data.news.value:

            print("Webpage Results#{}".format(len(web_data.news.value)))

            first_web_page = web_data.news.value[0]
            print("First web page name: {} ".format(first_web_page.name))
            print("First web page URL: {} ".format(first_web_page.url))

        else:
            print("Didn't see any Web data..")

    except Exception as err:
        print("Encountered exception. {}".format(err))


def web_search_with_answer_count_promote_and_safe_search(subscription_key):
    """WebSearchWithAnswerCountPromoteAndSafeSearch.

    This will search (Lady Gaga) with answerCount and promote parameters and print details of answers.
    """

    client = WebSearchClient(AzureKeyCredential(subscription_key))

    try:
        web_data = client.web.search(
            query="Lady Gaga",
            answer_count=2,
            promote=["videos"],
            safe_search=SafeSearch.strict,  # or directly "Strict"
        )
        print('Searched for Query# " Lady Gaga"')

        if web_data.web_pages.value:

            print("Webpage Results#{}".format(len(web_data.web_pages.value)))

            first_web_page = web_data.web_pages.value[0]
            print("First web page name: {} ".format(first_web_page.name))
            print("First web page URL: {} ".format(first_web_page.url))

        else:
            print("Didn't see any Web data..")

    except Exception as err:
        print("Encountered exception. {}".format(err))

def main() -> None:
    """Main function
    """ 
    dotenv_v = dotenv.dotenv_values()
    
    SUBSCRIPTION_KEY_ENV_VAR_NAME = "BING_SEARCH_V7_WEB_SEARCH_SUBSCRIPTION_KEY"
    subscription_key = dotenv_v.get(SUBSCRIPTION_KEY_ENV_VAR_NAME, os.environ.get(SUBSCRIPTION_KEY_ENV_VAR_NAME))
    
    result_types_lookup(subscription_key)
    web_results_with_count_and_offset(subscription_key)
    web_search_with_response_filter(subscription_key)
    web_search_with_answer_count_promote_and_safe_search(subscription_key)

if __name__ == "__main__":
    main()
