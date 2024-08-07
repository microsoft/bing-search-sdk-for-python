# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6320, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._web_search_client import WebSearchClient

__all__ = ["WebSearchClient"]

try:
    from ._patch import patch_sdk  # type: ignore

    patch_sdk()
except ImportError:
    pass
