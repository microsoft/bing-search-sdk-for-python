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


class Freshness(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    DAY = "Day"
    WEEK = "Week"
    MONTH = "Month"


class SafeSearch(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    OFF = "Off"
    MODERATE = "Moderate"
    STRICT = "Strict"


class TextFormat(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    RAW = "Raw"
    HTML = "Html"


class XBingApisSDK(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    TRUE = "true"
