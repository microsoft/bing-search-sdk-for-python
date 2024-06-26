# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Tests for Video Search REST samples."""

import unittest

import dotenv
from requests import HTTPError, JSONDecodeError

from samples.rest.bing_video_search_v7 import video_search_basic


class VideoSearchRESTSamplesTest(unittest.TestCase):
    """Class for testing REST samples."""

    @classmethod
    def setUpClass(cls):
        cls.env = dotenv.dotenv_values()

    def test_video_search_basic(self):
        """Test the basic REST call to Video Search API"""
        response = video_search_basic(
            "nature",
            subscription_key=self.env.get(
                "BING_SEARCH_V7_VIDEO_SEARCH_SUBSCRIPTION_KEY"
            ),
        )
        self.assertEqual(response.status_code, 200)

    def test_video_search_response_is_json(self):
        """Test that Video Search API returns responses in JSON format"""
        response = video_search_basic(
            "vim showcase",
            subscription_key=self.env.get(
                "BING_SEARCH_V7_VIDEO_SEARCH_SUBSCRIPTION_KEY"
            ),
        )
        try:
            response.json()
        except JSONDecodeError:
            self.fail(
                "Failed to decode response as JSON, check if valid JSON is returned"
            )

    def test_video_search_no_auth(self):
        """Test that Video Search API returns 401 if authorization fails"""
        with self.assertRaises(Exception) as ex:
            response = video_search_basic("kentucky derby", subscription_key="")
        self.assertEqual(type(ex.exception.__cause__), HTTPError)

    def test_video_search_response_object_type(self):
        """Test that Video Search API returns the correct type hint"""
        response = video_search_basic(
            "car relaxing drive",
            subscription_key=self.env.get(
                "BING_SEARCH_V7_VIDEO_SEARCH_SUBSCRIPTION_KEY"
            ),
        )
        try:
            self.assertEqual(response.json()["_type"], "Videos")
        except KeyError:
            self.fail("The response object doesn't include the type hint")

    def test_video_search_response_object_structure(self):
        """Test that Video Search API responses follow the correct structure"""
        response = video_search_basic(
            "how to download Teams",
            subscription_key=self.env.get(
                "BING_SEARCH_V7_VIDEO_SEARCH_SUBSCRIPTION_KEY"
            ),
        )
        response_json = response.json()
        self.assertGreater(response_json["totalEstimatedMatches"], 0)
        try:
            self.assertGreater(len(response_json["value"]), 0)
        except KeyError:
            self.fail("The response object doesn't include any video results")

    def test_video_search_required_parameter_query(self):
        """Test that Video Search API returns an error if required parameter is empty"""
        response = video_search_basic(
            subscription_key=self.env.get(
                "BING_SEARCH_V7_VIDEO_SEARCH_SUBSCRIPTION_KEY"
            ),
            query="",
        )
        try:
            self.assertEqual(response.json()["_type"], "ErrorResponse")
        except KeyError:
            self.fail(
                "The response object is not of type 'ErrorResponse' when the query is empty"
            )


if __name__ == "__main__":
    unittest.main(verbosity=1)
