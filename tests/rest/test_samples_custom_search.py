# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Tests for Custom Search REST samples."""

import unittest

import dotenv
from requests import JSONDecodeError

from samples.rest.bing_custom_search_v7 import custom_search_basic


class CustomSearchRESTSamplesTest(unittest.TestCase):
    """Class for testing REST samples."""

    @classmethod
    def setUpClass(cls):
        cls.env = dotenv.dotenv_values()
        cls.subscription_key = cls.env.get(
            "BING_SEARCH_V7_CUSTOM_SEARCH_SUBSCRIPTION_KEY"
        )
        cls.config_id = cls.env.get("BING_CUSTOM_SEARCH_CONFIG")

    def test_custom_search_subscription_key_not_empty(self):
        """Test that the subscription key is defined in the environment"""
        self.assertIsNotNone(self.subscription_key)
        self.assertNotEqual(self.subscription_key, "")

    def test_custom_search_basic(self):
        """Test the basic REST call to Custom Search API"""
        response = custom_search_basic(
            "microsoft",
            subscription_key=self.subscription_key,
            custom_config_id=self.config_id,
        )
        self.assertEqual(response.status_code, 200)

    def test_custom_search_response_is_json(self):
        """Test that Custom Search API returns responses in JSON format"""
        response = custom_search_basic(
            "engine",
            subscription_key=self.subscription_key,
            custom_config_id=self.config_id,
        )
        try:
            response.json()
        except JSONDecodeError:
            self.fail(
                "Failed to decode response as JSON, check if valid JSON is returned"
            )

    def test_custom_search_no_auth(self):
        """Test that Custom Search API returns 401 if authorization fails"""
        response = custom_search_basic(
            "power", subscription_key="", custom_config_id=self.config_id
        )
        self.assertEqual(response.status_code, 401)

    def test_custom_search_response_object_type(self):
        """Test that Custom Search API returns the correct type hint"""
        response = custom_search_basic(
            "new",
            subscription_key=self.subscription_key,
            custom_config_id=self.config_id,
        )
        try:
            self.assertEqual(response.json()["_type"], "SearchResponse")
        except KeyError:
            self.fail("The response object doesn't include the type hint")

    def test_custom_search_response_object_structure(self):
        """Test that Custom Search API responses follow the correct structure"""
        response = custom_search_basic(
            "news",
            subscription_key=self.subscription_key,
            custom_config_id=self.config_id,
        )
        response_json = response.json()
        self.assertIn("webPages", response_json)
        self.assertGreater(response_json["webPages"]["totalEstimatedMatches"], 0)
        self.assertGreater(len(response_json["webPages"]["value"]), 0)
        self.assertIn("rankingResponse", response_json)


if __name__ == "__main__":
    unittest.main(verbosity=1)
