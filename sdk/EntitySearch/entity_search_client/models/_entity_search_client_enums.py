# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6320, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass


class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class AnswerType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ENTITIES = "Entities"
    PLACES = "Places"


class EntityQueryScenario(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The supported query scenario. This field is set to DominantEntity or DisambiguationItem. The
    field is set to DominantEntity if Bing determines that only a single entity satisfies the
    request. For example, a book, movie, person, or attraction. If multiple entities could satisfy
    the request, the field is set to DisambiguationItem. For example, if the request uses the
    generic title of a movie franchise, the entity's type would likely be DisambiguationItem. But,
    if the request specifies a specific title from the franchise, the entity's type would likely be
    DominantEntity.
    """

    DOMINANT_ENTITY = "DominantEntity"
    DOMINANT_ENTITY_WITH_DISAMBIGUATION = "DominantEntityWithDisambiguation"
    DISAMBIGUATION = "Disambiguation"
    LIST = "List"
    LIST_WITH_PIVOT = "ListWithPivot"


class EntityScenario(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The supported scenario."""

    DOMINANT_ENTITY = "DominantEntity"
    DISAMBIGUATION_ITEM = "DisambiguationItem"
    LIST_ITEM = "ListItem"


class EntityType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    GENERIC = "Generic"
    PERSON = "Person"
    PLACE = "Place"
    MEDIA = "Media"
    ORGANIZATION = "Organization"
    LOCAL_BUSINESS = "LocalBusiness"
    RESTAURANT = "Restaurant"
    HOTEL = "Hotel"
    TOURIST_ATTRACTION = "TouristAttraction"
    TRAVEL = "Travel"
    CITY = "City"
    COUNTRY = "Country"
    ATTRACTION = "Attraction"
    HOUSE = "House"
    STATE = "State"
    RADIO_STATION = "RadioStation"
    STREET_ADDRESS = "StreetAddress"
    NEIGHBORHOOD = "Neighborhood"
    LOCALITY = "Locality"
    POSTAL_CODE = "PostalCode"
    REGION = "Region"
    SUB_REGION = "SubRegion"
    MINOR_REGION = "MinorRegion"
    CONTINENT = "Continent"
    POINT_OF_INTEREST = "PointOfInterest"
    OTHER = "Other"
    MOVIE = "Movie"
    BOOK = "Book"
    TELEVISION_SHOW = "TelevisionShow"
    TELEVISION_SEASON = "TelevisionSeason"
    VIDEO_GAME = "VideoGame"
    MUSIC_ALBUM = "MusicAlbum"
    MUSIC_RECORDING = "MusicRecording"
    MUSIC_GROUP = "MusicGroup"
    COMPOSITION = "Composition"
    THEATER_PLAY = "TheaterPlay"
    EVENT = "Event"
    ACTOR = "Actor"
    ARTIST = "Artist"
    ATTORNEY = "Attorney"
    SPECIALITY = "Speciality"
    COLLEGE_OR_UNIVERSITY = "CollegeOrUniversity"
    SCHOOL = "School"
    FOOD = "Food"
    DRUG = "Drug"
    ANIMAL = "Animal"
    SPORTS_TEAM = "SportsTeam"
    PRODUCT = "Product"
    CAR = "Car"


class ErrorCode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The error code that identifies the category of error."""

    NONE = "None"
    SERVER_ERROR = "ServerError"
    INVALID_REQUEST = "InvalidRequest"
    RATE_LIMIT_EXCEEDED = "RateLimitExceeded"
    INVALID_AUTHORIZATION = "InvalidAuthorization"
    INSUFFICIENT_AUTHORIZATION = "InsufficientAuthorization"


class ErrorSubCode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The error code that further helps to identify the error."""

    UNEXPECTED_ERROR = "UnexpectedError"
    RESOURCE_ERROR = "ResourceError"
    NOT_IMPLEMENTED = "NotImplemented"
    PARAMETER_MISSING = "ParameterMissing"
    PARAMETER_INVALID_VALUE = "ParameterInvalidValue"
    HTTP_NOT_ALLOWED = "HttpNotAllowed"
    BLOCKED = "Blocked"
    AUTHORIZATION_MISSING = "AuthorizationMissing"
    AUTHORIZATION_REDUNDANCY = "AuthorizationRedundancy"
    AUTHORIZATION_DISABLED = "AuthorizationDisabled"
    AUTHORIZATION_EXPIRED = "AuthorizationExpired"


class ResponseFormat(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    JSON = "Json"
    JSON_LD = "JsonLd"


class SafeSearch(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    OFF = "Off"
    MODERATE = "Moderate"
    STRICT = "Strict"


class XBingApisSDK(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    TRUE = "true"
