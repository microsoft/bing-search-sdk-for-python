# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6320, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import CustomImageSearchClientConfiguration
from .operations import CustomInstanceOperations
from .. import models


class CustomImageSearchClient(object):
    """The Bing Custom Image Search API lets you send an image search query to Bing and get back image search results customized to meet your custom search definition.

    :ivar custom_instance: CustomInstanceOperations operations
    :vartype custom_instance: custom_image_search_client.aio.operations.CustomInstanceOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = "https://api.bing.microsoft.com/v7.0/custom"
        self._config = CustomImageSearchClientConfiguration(credential, **kwargs)
        self._client = AsyncPipelineClient(
            base_url=base_url, config=self._config, **kwargs
        )

        client_models = {
            k: v for k, v in models.__dict__.items() if isinstance(v, type)
        }
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.custom_instance = CustomInstanceOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "CustomImageSearchClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
