# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import os
from spell_check_client import SpellCheckClient
from azure.core.credentials import AzureKeyCredential
import dotenv


ENDPOINT = "https://api.bing.microsoft.com" + "/v7.0/"


def spellcheck(subscription_key):
    """SpellCheck.

    This will do a search for misspelled query and parse the response.
    """
    client = SpellCheckClient(AzureKeyCredential(subscription_key))

    try:
        result = client.spell_checker("Bill Gatas", mode="proof")
        print('Correction for Query# "bill gatas"')

        if result.flagged_tokens:
            first_spellcheck_result = result.flagged_tokens[0]

            print("SpellCheck result count: {}".format(len(result.flagged_tokens)))
            print("First SpellCheck token: {}".format(first_spellcheck_result.token))
            print("First SpellCheck type: {}".format(first_spellcheck_result.type))
            print(
                "First SpellCheck suggestion count: {}".format(
                    len(first_spellcheck_result.suggestions)
                )
            )

            if first_spellcheck_result.suggestions:
                first_suggestion = first_spellcheck_result.suggestions[0]
                print(
                    "First SpellCheck suggestion score: {}".format(
                        first_suggestion.score
                    )
                )
                print(
                    "First SpellCheck suggestion: {}".format(
                        first_suggestion.suggestion
                    )
                )
            else:
                print("Couldn't get any Spell check results!")

        else:
            print("Didn't see any SpellCheck results..")

    except Exception as err:
        print("Encountered exception. {}".format(err))

def main() -> None:
    """Main function
    """ 
    dotenv_v = dotenv.dotenv_values()
    
    SUBSCRIPTION_KEY_ENV_VAR_NAME = "BING_SEARCH_V7_SPELL_CHECK_SUBSCRIPTION_KEY"
    subscription_key = dotenv_v.get(SUBSCRIPTION_KEY_ENV_VAR_NAME, os.environ.get(SUBSCRIPTION_KEY_ENV_VAR_NAME))

    spellcheck(subscription_key)


if __name__ == "__main__":
    main()
