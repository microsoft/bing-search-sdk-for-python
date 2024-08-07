# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6320, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ResponseBase(msrest.serialization.Model):
    """ResponseBase.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: Identifiable.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    """

    _validation = {
        "type": {"required": True},
    }

    _attribute_map = {
        "type": {"key": "_type", "type": "str"},
    }

    _subtype_map = {"type": {"Identifiable": "Identifiable"}}

    def __init__(self, **kwargs):
        super(ResponseBase, self).__init__(**kwargs)
        self.type = None  # type: Optional[str]


class Identifiable(ResponseBase):
    """Defines the identity of a resource.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: Answer, ErrorResponse, Response, SpellCheck.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    """

    _validation = {
        "type": {"required": True},
        "id": {"readonly": True},
    }

    _attribute_map = {
        "type": {"key": "_type", "type": "str"},
        "id": {"key": "id", "type": "str"},
    }

    _subtype_map = {
        "type": {
            "Answer": "Answer",
            "ErrorResponse": "ErrorResponse",
            "Response": "Response",
            "SpellCheck": "SpellCheck",
        }
    }

    def __init__(self, **kwargs):
        super(Identifiable, self).__init__(**kwargs)
        self.type = "Identifiable"  # type: str
        self.id = None


class Answer(Identifiable):
    """Answer.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    """

    _validation = {
        "type": {"required": True},
        "id": {"readonly": True},
    }

    _attribute_map = {
        "type": {"key": "_type", "type": "str"},
        "id": {"key": "id", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(Answer, self).__init__(**kwargs)
        self.type = "Answer"  # type: str


class Error(msrest.serialization.Model):
    """Defines the error that occurred.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. The error code that identifies the category of error. Possible values
     include: "None", "ServerError", "InvalidRequest", "RateLimitExceeded", "InvalidAuthorization",
     "InsufficientAuthorization". Default value: "None".
    :type code: str or ~spell_check_client.models.ErrorCode
    :ivar sub_code: The error code that further helps to identify the error. Possible values
     include: "UnexpectedError", "ResourceError", "NotImplemented", "ParameterMissing",
     "ParameterInvalidValue", "HttpNotAllowed", "Blocked", "AuthorizationMissing",
     "AuthorizationRedundancy", "AuthorizationDisabled", "AuthorizationExpired".
    :vartype sub_code: str or ~spell_check_client.models.ErrorSubCode
    :param message: Required. A description of the error.
    :type message: str
    :ivar more_details: A description that provides additional information about the error.
    :vartype more_details: str
    :ivar parameter: The parameter in the request that caused the error.
    :vartype parameter: str
    :ivar value: The parameter's value in the request that was not valid.
    :vartype value: str
    """

    _validation = {
        "code": {"required": True},
        "sub_code": {"readonly": True},
        "message": {"required": True},
        "more_details": {"readonly": True},
        "parameter": {"readonly": True},
        "value": {"readonly": True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "sub_code": {"key": "subCode", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "more_details": {"key": "moreDetails", "type": "str"},
        "parameter": {"key": "parameter", "type": "str"},
        "value": {"key": "value", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.code = kwargs.get("code", "None")
        self.sub_code = None
        self.message = kwargs["message"]
        self.more_details = None
        self.parameter = None
        self.value = None


class ErrorResponse(Identifiable):
    """The top-level response that represents a failed request.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :param errors: Required. A list of errors that describe the reasons why the request failed.
    :type errors: list[~spell_check_client.models.Error]
    """

    _validation = {
        "type": {"required": True},
        "id": {"readonly": True},
        "errors": {"required": True},
    }

    _attribute_map = {
        "type": {"key": "_type", "type": "str"},
        "id": {"key": "id", "type": "str"},
        "errors": {"key": "errors", "type": "[Error]"},
    }

    def __init__(self, **kwargs):
        super(ErrorResponse, self).__init__(**kwargs)
        self.type = "ErrorResponse"  # type: str
        self.errors = kwargs["errors"]


class Response(Identifiable):
    """Defines a response. All schemas that could be returned at the root of a response should inherit from this.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    """

    _validation = {
        "type": {"required": True},
        "id": {"readonly": True},
    }

    _attribute_map = {
        "type": {"key": "_type", "type": "str"},
        "id": {"key": "id", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(Response, self).__init__(**kwargs)
        self.type = "Response"  # type: str


class SpellCheck(Identifiable):
    """SpellCheck.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :ivar id: A String identifier.
    :vartype id: str
    :param flagged_tokens: Required.
    :type flagged_tokens: list[~spell_check_client.models.SpellingFlaggedToken]
    """

    _validation = {
        "type": {"required": True},
        "id": {"readonly": True},
        "flagged_tokens": {"required": True},
    }

    _attribute_map = {
        "type": {"key": "_type", "type": "str"},
        "id": {"key": "id", "type": "str"},
        "flagged_tokens": {"key": "flaggedTokens", "type": "[SpellingFlaggedToken]"},
    }

    def __init__(self, **kwargs):
        super(SpellCheck, self).__init__(**kwargs)
        self.type = "SpellCheck"  # type: str
        self.flagged_tokens = kwargs["flagged_tokens"]


class SpellingFlaggedToken(msrest.serialization.Model):
    """SpellingFlaggedToken.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param offset: Required.
    :type offset: int
    :param token: Required.
    :type token: str
    :param type: Required.  Possible values include: "UnknownToken", "RepeatedToken". Default
     value: "UnknownToken".
    :type type: str or ~spell_check_client.models.ErrorType
    :ivar suggestions:
    :vartype suggestions: list[~spell_check_client.models.SpellingTokenSuggestion]
    :ivar ping_url_suffix:
    :vartype ping_url_suffix: str
    """

    _validation = {
        "offset": {"required": True},
        "token": {"required": True},
        "type": {"required": True},
        "suggestions": {"readonly": True},
        "ping_url_suffix": {"readonly": True},
    }

    _attribute_map = {
        "offset": {"key": "offset", "type": "int"},
        "token": {"key": "token", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "suggestions": {"key": "suggestions", "type": "[SpellingTokenSuggestion]"},
        "ping_url_suffix": {"key": "pingUrlSuffix", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(SpellingFlaggedToken, self).__init__(**kwargs)
        self.offset = kwargs["offset"]
        self.token = kwargs["token"]
        self.type = kwargs.get("type", "UnknownToken")
        self.suggestions = None
        self.ping_url_suffix = None


class SpellingTokenSuggestion(msrest.serialization.Model):
    """SpellingTokenSuggestion.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param suggestion: Required.
    :type suggestion: str
    :ivar score:
    :vartype score: float
    :ivar ping_url_suffix:
    :vartype ping_url_suffix: str
    """

    _validation = {
        "suggestion": {"required": True},
        "score": {"readonly": True},
        "ping_url_suffix": {"readonly": True},
    }

    _attribute_map = {
        "suggestion": {"key": "suggestion", "type": "str"},
        "score": {"key": "score", "type": "float"},
        "ping_url_suffix": {"key": "pingUrlSuffix", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(SpellingTokenSuggestion, self).__init__(**kwargs)
        self.suggestion = kwargs["suggestion"]
        self.score = None
        self.ping_url_suffix = None
