
import os
from custom_search_client import CustomSearchClient
from azure.core.credentials import AzureKeyCredential

SUBSCRIPTION_KEY = None
ENDPOINT = "https://api.bing.microsoft.com"+  "/v7.0/"

def custom_search_web_page_result_lookup(subscription_key):
    """CustomSearch.

    This will look up a single query (Xbox) and print out name and url for first web result.
    """

    client = CustomSearchClient(
        endpoint=ENDPOINT,
        credential=AzureKeyCredential(subscription_key))

    try:
        web_data = client.custom_instance.search(query="xbox", custom_config=1)
        print("Searched for Query 'xbox'")

        if web_data.web_pages.value:
            first_web_result = web_data.web_pages.value[0]
            print("Web Pages result count: {}".format(
                len(web_data.web_pages.value)))
            print("First Web Page name: {}".format(first_web_result.name))
            print("First Web Page url: {}".format(first_web_result.url))
        else:
            print("Didn't see any web data..")

    except Exception as err:
        print("Encountered exception. {}".format(err))


if __name__ == "__main__":
    import sys, os.path
    sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
    custom_search_web_page_result_lookup(SUBSCRIPTION_KEY)
