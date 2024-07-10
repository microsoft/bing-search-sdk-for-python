# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6320, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models as _models

T = TypeVar("T")
ClsType = Optional[
    Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]
]


class AutoSuggestClientOperationsMixin:

    async def auto_suggest(
        self,
        x_bing_apis_sdk: Union[str, "_models.XBingApisSDK"],
        query: str,
        accept: Optional[str] = None,
        accept_language: Optional[str] = None,
        pragma: Optional[str] = None,
        user_agent_parameter: Optional[str] = None,
        client_id: Optional[str] = None,
        client_ip: Optional[str] = None,
        location: Optional[str] = None,
        country_code: Optional[str] = None,
        market: Optional[str] = "en-us",
        safe_search: Optional[Union[str, "_models.SafeSearch"]] = None,
        set_lang: Optional[str] = None,
        response_format: Optional[List[Union[str, "_models.ResponseFormat"]]] = None,
        **kwargs
    ) -> "_models.Suggestions":
        """The AutoSuggest API lets you send a search query to Bing and get back a list of query suggestions. This section provides technical details about the query parameters and headers that you use to request suggestions and the JSON response objects that contain them.

        The AutoSuggest API lets you send a search query to Bing and get back a list of query
        suggestions. This section provides technical details about the query parameters and headers
        that you use to request suggestions and the JSON response objects that contain them.

        :param x_bing_apis_sdk: Activate swagger compliance.
        :type x_bing_apis_sdk: str or ~auto_suggest_client.models.XBingApisSDK
        :param query: The user's search term.
        :type query: str
        :param accept: The default media type is application/json. To specify that the response use
         `JSON-LD <http://json-ld.org/>`_\ , set the Accept header to application/ld+json.
        :type accept: str
        :param accept_language: A comma-delimited list of one or more languages to use for user
         interface strings. The list is in decreasing order of preference. For additional information,
         including expected format, see `RFC2616
         <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>`_. This header and the setLang query
         parameter are mutually exclusive; do not specify both. If you set this header, you must also
         specify the `cc <https://docs.microsoft.com/en-us/bing/bing-autosuggest/overview>`_ query
         parameter. To determine the market to return results for, Bing uses the first supported
         language it finds from the list and combines it with the cc parameter value. If the list does
         not include a supported language, Bing finds the closest language and market that supports the
         request or it uses an aggregated or default market for the results. To determine the market
         that Bing used, see the BingAPIs-Market header. Use this header and the cc query parameter only
         if you specify multiple languages. Otherwise, use the `mkt <https://docs.microsoft.com/en-
         us/bing/bing-autosuggest/overview>`_ and `setLang <https://docs.microsoft.com/en-us/bing/bing-
         autosuggest/overview>`_ query parameters. A user interface string is a string that's used as a
         label in a user interface. There are few user interface strings in the JSON response objects.
         Any links to Bing.com properties in the response objects apply the specified language.
        :type accept_language: str
        :param pragma: By default, Bing returns cached content, if available. To prevent Bing from
         returning cached content, set the Pragma header to no-cache (for example, Pragma: no-cache).
        :type pragma: str
        :param user_agent_parameter: The user agent originating the request. Bing uses the user agent
         to provide mobile users with an optimized experience. Although optional, you are encouraged to
         always specify this header. The user-agent should be the same string that any commonly used
         browser sends. For information about user agents, see `RFC 2616
         <http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html>`_. The following are examples of user-
         agent strings. Windows Phone: Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0;
         Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 822). Android: Mozilla / 5.0 (Linux; U;
         Android 2.3.5; en - us; SCH - I500 Build / GINGERBREAD) AppleWebKit / 533.1 (KHTML; like Gecko)
         Version / 4.0 Mobile Safari / 533.1. iPhone: Mozilla / 5.0 (iPhone; CPU iPhone OS 6_1 like Mac
         OS X) AppleWebKit / 536.26 (KHTML; like Gecko) Mobile / 10B142 iPhone4; 1 BingWeb /
         3.03.1428.20120423. PC: Mozilla / 5.0 (Windows NT 6.3; WOW64; Trident / 7.0; Touch; rv:11.0)
         like Gecko. iPad: Mozilla / 5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit / 537.51.1 (KHTML,
         like Gecko) Version / 7.0 Mobile / 11A465 Safari / 9537.53.
        :type user_agent_parameter: str
        :param client_id: Bing uses this header to provide users with consistent behavior across Bing
         API calls. Bing often flights new features and improvements, and it uses the client ID as a key
         for assigning traffic on different flights. If you do not use the same client ID for a user
         across multiple requests, then Bing may assign the user to multiple conflicting flights. Being
         assigned to multiple conflicting flights can lead to an inconsistent user experience. For
         example, if the second request has a different flight assignment than the first, the experience
         may be unexpected. Also, Bing can use the client ID to tailor web results to that client ID’s
         search history, providing a richer experience for the user. Bing also uses this header to help
         improve result rankings by analyzing the activity generated by a client ID. The relevance
         improvements help with better quality of results delivered by Bing APIs and in turn enables
         higher click-through rates for the API consumer. IMPORTANT: Although optional, you should
         consider this header required. Persisting the client ID across multiple requests for the same
         end user and device combination enables 1) the API consumer to receive a consistent user
         experience, and 2) higher click-through rates via better quality of results from the Bing APIs.
         Each user that uses your application on the device must have a unique, Bing generated client
         ID. If you do not include this header in the request, Bing generates an ID and returns it in
         the X-MSEdge-ClientID response header. The only time that you should NOT include this header in
         a request is the first time the user uses your app on that device. Use the client ID for each
         Bing API request that your app makes for this user on the device. Persist the client ID. To
         persist the ID in a browser app, use a persistent HTTP cookie to ensure the ID is used across
         all sessions. Do not use a session cookie. For other apps such as mobile apps, use the device's
         persistent storage to persist the ID. The next time the user uses your app on that device, get
         the client ID that you persisted. Bing responses may or may not include this header. If the
         response includes this header, capture the client ID and use it for all subsequent Bing
         requests for the user on that device. If you include the X-MSEdge-ClientID, you must not
         include cookies in the request.
        :type client_id: str
        :param client_ip: The IPv4 or IPv6 address of the client device. The IP address is used to
         discover the user's location. Bing uses the location information to determine safe search
         behavior. Although optional, you are encouraged to always specify this header and the X-Search-
         Location header. Do not obfuscate the address (for example, by changing the last octet to 0).
         Obfuscating the address results in the location not being anywhere near the device's actual
         location, which may result in Bing serving erroneous results.
        :type client_ip: str
        :param location: A semicolon-delimited list of key/value pairs that describe the client's
         geographical location. Bing uses the location information to determine safe search behavior and
         to return relevant local content. Specify the key/value pair as :code:`<key>`::code:`<value>`.
         The following are the keys that you use to specify the user's location. lat (required): The
         latitude of the client's location, in degrees. The latitude must be greater than or equal to
         -90.0 and less than or equal to +90.0. Negative values indicate southern latitudes and positive
         values indicate northern latitudes. long (required): The longitude of the client's location, in
         degrees. The longitude must be greater than or equal to -180.0 and less than or equal to
         +180.0. Negative values indicate western longitudes and positive values indicate eastern
         longitudes. re (required): The radius, in meters, which specifies the horizontal accuracy of
         the coordinates. Pass the value returned by the device's location service. Typical values might
         be 22m for GPS/Wi-Fi, 380m for cell tower triangulation, and 18,000m for reverse IP lookup. ts
         (optional): The UTC UNIX timestamp of when the client was at the location. (The UNIX timestamp
         is the number of seconds since January 1, 1970.) head (optional): The client's relative heading
         or direction of travel. Specify the direction of travel as degrees from 0 through 360, counting
         clockwise relative to true north. Specify this key only if the sp key is nonzero. sp
         (optional): The horizontal velocity (speed), in meters per second, that the client device is
         traveling. alt (optional): The altitude of the client device, in meters. are (optional): The
         radius, in meters, that specifies the vertical accuracy of the coordinates. Specify this key
         only if you specify the alt key. Although many of the keys are optional, the more information
         that you provide, the more accurate the location results are. Although optional, you are
         encouraged to always specify the user's geographical location. Providing the location is
         especially important if the client's IP address does not accurately reflect the user's physical
         location (for example, if the client uses VPN). For optimal results, you should include this
         header and the X-MSEdge-ClientIP header, but at a minimum, you should include this header.
        :type location: str
        :param country_code: A 2-character country code of the country where the results come from.
         This API supports only the United States market. If you specify this query parameter, it must
         be set to us. If you set this parameter, you must also specify the Accept-Language header. Bing
         uses the first supported language it finds from the languages list, and combine that language
         with the country code that you specify to determine the market to return results for. If the
         languages list does not include a supported language, Bing finds the closest language and
         market that supports the request, or it may use an aggregated or default market for the results
         instead of a specified one. You should use this query parameter and the Accept-Language query
         parameter only if you specify multiple languages; otherwise, you should use the mkt and setLang
         query parameters. This parameter and the mkt query parameter are mutually exclusive—do not
         specify both.
        :type country_code: str
        :param market: The market where the results come from. You are strongly encouraged to always
         specify the market, if known. Specifying the market helps Bing route the request and return an
         appropriate and optimal response. This parameter and the cc query parameter are mutually
         exclusive—do not specify both.
        :type market: str
        :param safe_search: Filter suggestions for adult content. The following are the possible filter
         values. Off: Return suggestions with adult text, images, or videos. Moderate: Return suggestion
         with adult text but not adult images or videos. Strict: Do not return news articles with adult
         text, images, or videos. If the request comes from a market that Bing's adult policy requires
         that safeSearch is set to Strict, Bing ignores the safeSearch value and uses Strict. If you use
         the site: query operator, there is the chance that the response may contain adult content
         regardless of what the safeSearch query parameter is set to. Use site: only if you are aware of
         the content on the site and your scenario supports the possibility of adult content.
        :type safe_search: str or ~auto_suggest_client.models.SafeSearch
        :param set_lang: The language to use for user interface strings. Specify the language using the
         ISO 639-1 2-letter language code. For example, the language code for English is EN. The default
         is EN (English). Although optional, you should always specify the language. Typically, you set
         setLang to the same language specified by mkt unless the user wants the user interface strings
         displayed in a different language. This parameter and the Accept-Language header are mutually
         exclusive; do not specify both. A user interface string is a string that's used as a label in a
         user interface. There are few user interface strings in the JSON response objects. Also, any
         links to Bing.com properties in the response objects apply the specified language.
        :type set_lang: str
        :param response_format: The media type to use for the response. The following are the possible
         case-insensitive values: JSON, JSONLD. The default is JSON. If you specify JSONLD, the response
         body includes JSON-LD objects that contain the search results.
        :type response_format: list[str or ~auto_suggest_client.models.ResponseFormat]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Suggestions, or the result of cls(response)
        :rtype: ~auto_suggest_client.models.Suggestions
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Suggestions"]
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
        }
        error_map.update(kwargs.pop("error_map", {}))

        # Construct URL
        url = self.auto_suggest.metadata["url"]  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if country_code is not None:
            query_parameters["cc"] = self._serialize.query(
                "country_code", country_code, "str"
            )
        if market is not None:
            query_parameters["mkt"] = self._serialize.query("market", market, "str")
        query_parameters["q"] = self._serialize.query("query", query, "str")
        if safe_search is not None:
            query_parameters["safeSearch"] = self._serialize.query(
                "safe_search", safe_search, "str"
            )
        if set_lang is not None:
            query_parameters["setLang"] = self._serialize.query(
                "set_lang", set_lang, "str"
            )
        if response_format is not None:
            query_parameters["ResponseFormat"] = self._serialize.query(
                "response_format", response_format, "[str]", div=","
            )

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters["X-BingApis-SDK"] = self._serialize.header(
            "x_bing_apis_sdk", x_bing_apis_sdk, "str"
        )
        if accept is not None:
            header_parameters["Accept"] = self._serialize.header(
                "accept", accept, "str"
            )
        if accept_language is not None:
            header_parameters["Accept-Language"] = self._serialize.header(
                "accept_language", accept_language, "str"
            )
        if pragma is not None:
            header_parameters["Pragma"] = self._serialize.header(
                "pragma", pragma, "str"
            )
        if user_agent_parameter is not None:
            header_parameters["User-Agent"] = self._serialize.header(
                "user_agent_parameter", user_agent_parameter, "str"
            )
        if client_id is not None:
            header_parameters["X-MSEdge-ClientID"] = self._serialize.header(
                "client_id", client_id, "str"
            )
        if client_ip is not None:
            header_parameters["X-MSEdge-ClientIP"] = self._serialize.header(
                "client_ip", client_ip, "str"
            )
        if location is not None:
            header_parameters["X-Search-Location"] = self._serialize.header(
                "location", location, "str"
            )

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(
                status_code=response.status_code, response=response, error_map=error_map
            )
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Suggestions", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    auto_suggest.metadata = {"url": "/Suggestions"}  # type: ignore
