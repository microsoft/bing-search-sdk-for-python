# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6320, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Answer
    from ._models_py3 import Error
    from ._models_py3 import ErrorResponse
    from ._models_py3 import Identifiable
    from ._models_py3 import Response
    from ._models_py3 import ResponseBase
    from ._models_py3 import SpellCheck
    from ._models_py3 import SpellingFlaggedToken
    from ._models_py3 import SpellingTokenSuggestion
except (SyntaxError, ImportError):
    from ._models import Answer  # type: ignore
    from ._models import Error  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import Identifiable  # type: ignore
    from ._models import Response  # type: ignore
    from ._models import ResponseBase  # type: ignore
    from ._models import SpellCheck  # type: ignore
    from ._models import SpellingFlaggedToken  # type: ignore
    from ._models import SpellingTokenSuggestion  # type: ignore

from ._spell_check_client_enums import (
    ActionType,
    ErrorCode,
    ErrorSubCode,
    ErrorType,
    Mode,
    XBingApisSDK,
)

__all__ = [
    "Answer",
    "Error",
    "ErrorResponse",
    "Identifiable",
    "Response",
    "ResponseBase",
    "SpellCheck",
    "SpellingFlaggedToken",
    "SpellingTokenSuggestion",
    "ActionType",
    "ErrorCode",
    "ErrorSubCode",
    "ErrorType",
    "Mode",
    "XBingApisSDK",
]
