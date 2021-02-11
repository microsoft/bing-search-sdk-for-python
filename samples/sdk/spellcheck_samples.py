import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
parent_dir2 = os.path.dirname(parent_dir)
sys.path.insert(0, parent_dir2)

from sdk.SpellCheck.spell_check_client._spell_check_client import SpellCheckClient
from azure.core.credentials import AzureKeyCredential
sys.path.insert(0, current_dir)
# Add your Bing Spell Check subscription key to your environment variables.
#SUBSCRIPTION_KEY = os.environ['BING_SPELL_CHECK_SUBSCRIPTION_KEY']

SUBSCRIPTION_KEY =  None
ENDPOINT = "https://api.bing.microsoft.com"+  "/v7.0/"

def spellcheck(subscription_key):
    """SpellCheck.

    This will do a search for misspelled query and parse the response.
    """
    client = SpellCheckClient(AzureKeyCredential(subscription_key))

    try:
        result = client.spell_checker("Bill Gatas", mode="proof")
        print("Correction for Query# \"bill gatas\"")

        if result.flagged_tokens:
            first_spellcheck_result = result.flagged_tokens[0]

            print("SpellCheck result count: {}".format(
                len(result.flagged_tokens)))
            print("First SpellCheck token: {}".format(
                first_spellcheck_result.token))
            print("First SpellCheck type: {}".format(
                first_spellcheck_result.type))
            print("First SpellCheck suggestion count: {}".format(
                len(first_spellcheck_result.suggestions)))

            if first_spellcheck_result.suggestions:
                first_suggestion = first_spellcheck_result.suggestions[0]
                print("First SpellCheck suggestion score: {}".format(
                    first_suggestion.score))
                print("First SpellCheck suggestion: {}".format(
                    first_suggestion.suggestion))
            else:
                print("Couldn't get any Spell check results!")

        else:
            print("Didn't see any SpellCheck results..")

    except Exception as err:
        print("Encountered exception. {}".format(err))


if __name__ == "__main__":
    import sys, os.path
    sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
    spellcheck(SUBSCRIPTION_KEY)
