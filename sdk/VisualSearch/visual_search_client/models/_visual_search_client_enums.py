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


class Currency(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The monetary currency. For example, USD."""

    USD = "USD"
    CAD = "CAD"
    GBP = "GBP"
    EUR = "EUR"
    COP = "COP"
    JPY = "JPY"
    CNY = "CNY"
    AUD = "AUD"
    INR = "INR"
    AED = "AED"
    AFN = "AFN"
    ALL = "ALL"
    AMD = "AMD"
    ANG = "ANG"
    AOA = "AOA"
    ARS = "ARS"
    AWG = "AWG"
    AZN = "AZN"
    BAM = "BAM"
    BBD = "BBD"
    BDT = "BDT"
    BGN = "BGN"
    BHD = "BHD"
    BIF = "BIF"
    BMD = "BMD"
    BND = "BND"
    BOB = "BOB"
    BOV = "BOV"
    BRL = "BRL"
    BSD = "BSD"
    BTN = "BTN"
    BWP = "BWP"
    BYR = "BYR"
    BZD = "BZD"
    CDF = "CDF"
    CHE = "CHE"
    CHF = "CHF"
    CHW = "CHW"
    CLF = "CLF"
    CLP = "CLP"
    COU = "COU"
    CRC = "CRC"
    CUC = "CUC"
    CUP = "CUP"
    CVE = "CVE"
    CZK = "CZK"
    DJF = "DJF"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EGP = "EGP"
    ERN = "ERN"
    ETB = "ETB"
    FJD = "FJD"
    FKP = "FKP"
    GEL = "GEL"
    GHS = "GHS"
    GIP = "GIP"
    GMD = "GMD"
    GNF = "GNF"
    GTQ = "GTQ"
    GYD = "GYD"
    HKD = "HKD"
    HNL = "HNL"
    HRK = "HRK"
    HTG = "HTG"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    IQD = "IQD"
    IRR = "IRR"
    ISK = "ISK"
    JMD = "JMD"
    JOD = "JOD"
    KES = "KES"
    KGS = "KGS"
    KHR = "KHR"
    KMF = "KMF"
    KPW = "KPW"
    KRW = "KRW"
    KWD = "KWD"
    KYD = "KYD"
    KZT = "KZT"
    LAK = "LAK"
    LBP = "LBP"
    LKR = "LKR"
    LRD = "LRD"
    LSL = "LSL"
    LYD = "LYD"
    MAD = "MAD"
    MDL = "MDL"
    MGA = "MGA"
    MKD = "MKD"
    MMK = "MMK"
    MNT = "MNT"
    MOP = "MOP"
    MRO_ENUM = "MRO"
    MUR = "MUR"
    MVR = "MVR"
    MWK = "MWK"
    MXN = "MXN"
    MXV = "MXV"
    MYR = "MYR"
    MZN = "MZN"
    NAD = "NAD"
    NGN = "NGN"
    NIO = "NIO"
    NOK = "NOK"
    NPR = "NPR"
    NZD = "NZD"
    OMR = "OMR"
    PAB = "PAB"
    PEN = "PEN"
    PGK = "PGK"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    RWF = "RWF"
    SAR = "SAR"
    SBD = "SBD"
    SCR = "SCR"
    SDG = "SDG"
    SEK = "SEK"
    SGD = "SGD"
    SHP = "SHP"
    SLL = "SLL"
    SOS = "SOS"
    SRD = "SRD"
    SSP = "SSP"
    STD = "STD"
    SYP = "SYP"
    SZL = "SZL"
    THB = "THB"
    TJS = "TJS"
    TMT = "TMT"
    TND = "TND"
    TOP = "TOP"
    TRY_ENUM = "TRY"
    TTD = "TTD"
    TWD = "TWD"
    TZS = "TZS"
    UAH = "UAH"
    UGX = "UGX"
    UYU = "UYU"
    UZS = "UZS"
    VEF = "VEF"
    VND = "VND"
    VUV = "VUV"
    WST = "WST"
    XAF = "XAF"
    XCD = "XCD"
    XOF = "XOF"
    XPF = "XPF"
    YER = "YER"
    ZAR = "ZAR"
    ZMW = "ZMW"


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


class ItemAvailability(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The item's availability. The following are the possible values: Discontinued, InStock,
    InStoreOnly, LimitedAvailability, OnlineOnly, OutOfStock, PreOrder, SoldOut.
    """

    DISCONTINUED = "Discontinued"
    IN_STOCK = "InStock"
    IN_STORE_ONLY = "InStoreOnly"
    LIMITED_AVAILABILITY = "LimitedAvailability"
    ONLINE_ONLY = "OnlineOnly"
    OUT_OF_STOCK = "OutOfStock"
    PRE_ORDER = "PreOrder"
    SOLD_OUT = "SoldOut"


class SafeSearch(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    OFF = "Off"
    MODERATE = "Moderate"
    STRICT = "Strict"


class XBingApisSDK(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    TRUE = "true"
