
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
parent_dir2 = os.path.dirname(parent_dir)
sys.path.insert(0, parent_dir2)
from sdk.Autosuggest.autosuggest_client._auto_suggest_client import AutoSuggestClient
from models._models import Suggestions, SuggestionsSuggestionGroup, SearchAction,ErrorResponse
from azure.core.credentials import AzureKeyCredential
sys.path.insert(0, current_dir)
# Add your Bing Autosuggest subscription key to your environment variables.


SUBSCRIPTION_KEY = None
ENDPOINT = "https://api.bing.microsoft.com"+  "/v7.0/"
def autosuggest_lookup(subscription_key):
    """AutoSuggestLookup.

    This will look up a single query (Xbox) and print out name and url for first web result.
    """
    client = AutoSuggestClient(
        endpoint=ENDPOINT,
        credential=AzureKeyCredential(SUBSCRIPTION_KEY)
    )

    try:
        suggestions = client.auto_suggest(
            query="Satya Nadella")  # type: Suggestions

        if suggestions.suggestion_groups:
            print("Searched for \"Satya Nadella\" and found suggestions:")
            suggestion_group = suggestions.suggestion_groups[0]  # type: SuggestionsSuggestionGroup
            for suggestion in suggestion_group.search_suggestions:  # type: SearchAction
                print("....................................")
                print(suggestion.query)
                print(suggestion.display_text)
                print(suggestion.url)
                print(suggestion.search_kind)
        else:
            print("Didn't see any suggestion..")

    except Exception as err:
        print("Encountered exception. {}".format(err))


def error(subscription_key):
    """Error.

    This triggers a bad request and shows how to read the error response.
    """

    # Breaking the subscription key on purpose
    client = AutoSuggestClient(
        credential=AzureKeyCredential(SUBSCRIPTION_KEY+'1'),
        endpoint=ENDPOINT
        
    )

    try:
        suggestions = client.auto_suggest(
            query="Satya Nadella", market="no-ty")
    except Exception as err:
        # The status code of the error should be a good indication of what occurred. However, if you'd like more details, you can dig into the response.
        # Please note that depending on the type of error, the response schema might be different, so you aren't guaranteed a specific error response schema.

        print("Exception occurred, with reason {}.\n".format( err))


if __name__ == "__main__":
    import sys
    import os.path
    sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..")))
    autosuggest_lookup(SUBSCRIPTION_KEY)
    error(SUBSCRIPTION_KEY)
