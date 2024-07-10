import os
from entity_search_client import EntitySearchClient
from entity_search_client.models import Place
from azure.core.credentials import AzureKeyCredential

SUBSCRIPTION_KEY = None
ENDPOINT = "https://api.bing.microsoft.com" + "/v7.0/"


def dominant_entity_lookup(subscription_key):
    """DominantEntityLookup.

    This will look up a single entity (Satya Nadella) and print out a short description about them.
    """
    client = EntitySearchClient(
        endpoint=ENDPOINT, credential=AzureKeyCredential(SUBSCRIPTION_KEY)
    )

    try:
        entity_data = client.entities.search(query="satya nadella")

        if entity_data.entities.value:
            # find the entity that represents the dominant one

            main_entities = [
                entity
                for entity in entity_data.entities.value
                if entity.entity_presentation_info.entity_scenario == "DominantEntity"
            ]

            if main_entities:
                print(
                    'Searched for "Satya Nadella" and found a dominant entity with this description:'
                )
                print(main_entities[0].description)
            else:
                print("Couldn't find main entity Satya Nadella!")

        else:
            print("Didn't see any data..")

    except Exception as err:
        print("Encountered exception. {}".format(err))


def handling_disambiguation(subscription_key):
    """HandlingDisambiguation.

    "This will handle disambiguation results for an ambiguous query (Williams parker)".
    """
    client = EntitySearchClient(
        endpoint=ENDPOINT, credential=AzureKeyCredential(SUBSCRIPTION_KEY)
    )

    try:
        entity_data = client.entities.search(query="Williams parker")

        if entity_data.entities:
            # find the entity that represents the dominant one

            main_entities = [
                entity
                for entity in entity_data.entities.value
                if entity.entity_presentation_info.entity_scenario == "DominantEntity"
            ]

            disambig_entities = [
                entity
                for entity in entity_data.entities.value
                if entity.entity_presentation_info.entity_scenario
                == "DisambiguationItem"
            ]

            if main_entities:
                main_entity = main_entities[0]
                type_hint = (
                    main_entity.entity_presentation_info.entity_type_display_hint
                )

                print(
                    'Searched for "Williams parker" and found a dominant entity {}with this description:'.format(
                        '"with type hint "{}" '.format(type_hint) if type_hint else ""
                    )
                )
                print(main_entity.description)
            else:
                print("Couldn't find a reliable dominant entity for Williams parker!")

            if disambig_entities:
                print(
                    "\nThis query is pretty ambiguous and can be referring to multiple things. Did you mean one of these:"
                )
                suggestions = []
                for disambig_entity in disambig_entities:
                    suggestions.append(
                        "{} the {}".format(
                            disambig_entity.name,
                            disambig_entity.entity_presentation_info.entity_type_display_hint,
                        )
                    )
                print(", or ".join(suggestions))
            else:
                print(
                    "We didn't find any disambiguation items for Williams parker, so we must be certain what you're talking about!"
                )

        else:
            print("Didn't see any data..")

    except Exception as err:
        print("Encountered exception. {}".format(err))


def restaurant_lookup(subscription_key):
    """RestaurantLookup.

    This will look up a single restaurant (john howie bellevue) and print out its phone number.
    """
    client = EntitySearchClient(
        endpoint=ENDPOINT, credential=AzureKeyCredential(SUBSCRIPTION_KEY)
    )

    try:
        entity_data = client.entities.search(query="john howie bellevue")

        if entity_data.places.value:

            restaurant = entity_data.places.value[0]

            # Some local entities will be places, others won't be. Depending on what class contains the data you want, you can check
            # using isinstance one of the class, or try to get the attribute and handle the exception (EAFP principle).
            # The recommended Python way is usually EAFP (see https://docs.python.org/3/glossary.html)
            # In this case, the item being returned is technically a Restaurant, but the Place schema has the data we want (telephone)

            # Pythonic approach : EAFP "Easier to ask for forgiveness than permission"
            try:
                url = restaurant.url
                print(
                    'Searched for "John Howie Bellevue" and found a restaurant with this website:'
                )
                print(url)
            except AttributeError:
                print("Couldn't find a place!")

        else:
            print("Didn't see any data..")

    except Exception as err:
        print("Encountered exception. {}".format(err))


def multiple_restaurant_lookup(subscription_key):
    """MultipleRestaurantLookup.

    This will look up a list of restaurants (seattle restaurants) and present their names and phone numbers.
    """

    client = EntitySearchClient(
        endpoint=ENDPOINT, credential=AzureKeyCredential(SUBSCRIPTION_KEY)
    )

    try:
        restaurants = client.entities.search(query="seattle restaurants")

        if restaurants.places.value:

            # get all the list items that relate to this query
            list_items = [
                entity
                for entity in restaurants.places.value
                if entity.entity_presentation_info.entity_scenario == "ListItem"
            ]

            if list_items:

                suggestions = []
                for place in list_items:
                    # Pythonic approach : EAFP "Easier to ask for forgiveness than permission"
                    # see https://docs.python.org/3/glossary.html
                    try:
                        suggestions.append("{} ({})".format(place.name, place.type))
                    except AttributeError:
                        print(
                            "Unexpectedly found something that isn't a place named '{}'",
                            place.name,
                        )

                print("Ok, we found these places: ")
                print(", ".join(suggestions))

            else:
                print('Couldn\'t find any relevant results for "seattle restaurants"')

        else:
            print("Didn't see any data..")

    except Exception as err:
        print("Encountered exception. {}".format(err))


def error(subscription_key):
    """Error.

    This triggers a bad request and shows how to read the error response.
    """

    client = EntitySearchClient(
        endpoint=ENDPOINT, credential=AzureKeyCredential(SUBSCRIPTION_KEY)
    )

    try:
        entity_data = client.entities.search(query="tom cruise", market="no-ty")
    except Exception as err:
        # The status code of the error should be a good indication of what occurred. However, if you'd like more details, you can dig into the response.
        # Please note that depending on the type of error, the response schema might be different, so you aren't guaranteed a specific error response schema.
        print("\n This sample is triggered with an error")
        print("\nException occurred, with reason {}.\n".format(err))


if __name__ == "__main__":
    import sys, os.path

    sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
    dominant_entity_lookup(SUBSCRIPTION_KEY)
    handling_disambiguation(SUBSCRIPTION_KEY)
    restaurant_lookup(SUBSCRIPTION_KEY)
    multiple_restaurant_lookup(SUBSCRIPTION_KEY)
    error(SUBSCRIPTION_KEY)
