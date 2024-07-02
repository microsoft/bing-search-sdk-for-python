# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Tests for Video Search REST samples."""

import os
import unittest

import dotenv
from requests import JSONDecodeError

from samples.rest.bing_video_search_v7 import video_search_basic


class VideoSearchRESTSamplesTest(unittest.TestCase):
    """Class for testing REST samples."""

    @classmethod
    def setUpClass(cls):
        cls.dotenv = dotenv.dotenv_values()
        subscription_key_env_var_name = "BING_SEARCH_V7_VIDEO_SEARCH_SUBSCRIPTION_KEY"
        cls.subscription_key = cls.dotenv.get(
            subscription_key_env_var_name, os.environ.get(subscription_key_env_var_name)
        )

    def test_video_search_subscription_key_not_empty(self):
        """Test that the subscription key is defined in the environment"""
        self.assertIsNotNone(self.subscription_key)
        self.assertNotEqual(self.subscription_key, "")

    def test_video_search_basic(self):
        """Test the basic REST call to Video Search API"""
        response = video_search_basic("nature", subscription_key=self.subscription_key)
        self.assertEqual(response.status_code, 200)

    def test_video_search_response_is_json(self):
        """Test that Video Search API returns responses in JSON format"""
        response = video_search_basic(
            "vim showcase", subscription_key=self.subscription_key
        )
        try:
            response.json()
        except JSONDecodeError:
            self.fail(
                "Failed to decode response as JSON, check if valid JSON is returned"
            )

    def test_video_search_no_auth(self):
        """Test that Video Search API returns 401 if authorization fails"""
        response = video_search_basic("kentucky derby", subscription_key="")
        self.assertEqual(response.status_code, 401)

    def test_video_search_response_object_type(self):
        """Test that Video Search API returns the correct type hint"""
        response = video_search_basic(
            "car relaxing drive", subscription_key=self.subscription_key
        )
        try:
            self.assertEqual(response.json()["_type"], "Videos")
        except KeyError:
            self.fail("The response object doesn't include the type hint")

    def test_video_search_response_object_structure(self):
        """Test that Video Search API responses follow the correct structure"""
        response = video_search_basic(
            "how to download Teams", subscription_key=self.subscription_key
        )
        response_json = response.json()
        self.assertGreater(response_json["totalEstimatedMatches"], 0)
        try:
            self.assertGreater(len(response_json["value"]), 0)
        except KeyError:
            self.fail("The response object doesn't include any video results")

    def test_video_search_required_parameter_query(self):
        """Test that Video Search API returns an error if a required parameter is missing"""
        response = video_search_basic(subscription_key=self.subscription_key, query="")
        self.assertEqual(response.status_code, 400)

    # pylint: disable=line-too-long
    # learn.microsoft.com/en-us/bing/search-apis/bing-video-search/reference/response-objects#errorresponse
    def test_video_search_error_response_object_structure(self):
        """Test the structure of the Error Response"""
        response = video_search_basic("", "")
        try:
            self.assertEqual(response.json()["_type"], "ErrorResponse")
        except KeyError:
            self.fail("The response object type hint is missing")


if __name__ == "__main__":
    unittest.main(verbosity=1)
