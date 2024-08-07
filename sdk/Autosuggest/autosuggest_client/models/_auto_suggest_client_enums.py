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


class ErrorCode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The error code that identifies the category of error."""

    NONE = "None"
    SERVER_ERROR = "ServerError"
    INVALID_REQUEST = "InvalidRequest"
    RATE_LIMIT_EXCEEDED = "RateLimitExceeded"
    INVALID_AUTHORIZATION = "InvalidAuthorization"
    INSUFFICIENT_AUTHORIZATION = "InsufficientAuthorization"


class ResponseFormat(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    JSON = "Json"
    JSON_LD = "JsonLd"


class SafeSearch(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    OFF = "Off"
    MODERATE = "Moderate"
    STRICT = "Strict"


class ScenarioType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    UNKNOWN = "Unknown"
    WEB = "Web"
    STORE_APPS = "StoreApps"
    SEARCH_HISTORY = "SearchHistory"
    PERSONAL_SEARCH_DOCUMENTS = "PersonalSearchDocuments"
    PERSONAL_SEARCH_TAGS = "PersonalSearchTags"
    CUSTOM = "Custom"


class SearchKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    WEB_SEARCH = "WebSearch"
    HISTORY_SEARCH = "HistorySearch"
    DOCUMENT_SEARCH = "DocumentSearch"
    TAG_SEARCH = "TagSearch"
    LOCATION_SEARCH = "LocationSearch"
    CUSTOM_SEARCH = "CustomSearch"


class XBingApisSDK(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    TRUE = "true"
