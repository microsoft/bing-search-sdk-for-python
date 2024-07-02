# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Tests for Web Search REST samples."""

import os
import unittest

import dotenv
import pytest
from requests import JSONDecodeError

from samples.rest.bing_web_search_v7 import web_search_basic


class WebSearchRESTSamplesTest(unittest.TestCase):
    """Class for testing REST samples."""

    @classmethod
    def setUpClass(cls):
        cls.dotenv = dotenv.dotenv_values()
        subscription_key_env_var_name = "BING_SEARCH_V7_WEB_SEARCH_SUBSCRIPTION_KEY"
        cls.subscription_key = cls.dotenv.get(
            subscription_key_env_var_name, os.environ.get(subscription_key_env_var_name)
        )

    def test_web_search_subscription_key_not_empty(self):
        """Test that the subscription key is defined in the environment"""
        self.assertIsNotNone(self.subscription_key)
        self.assertNotEqual(self.subscription_key, "")

    def test_web_search_basic(self):
        """Test the basic REST call to Web Search API"""
        response = web_search_basic("vim", subscription_key=self.subscription_key)
        self.assertEqual(response.status_code, 200)

    def test_web_search_response_is_json(self):
        """Test that Web Search API returns responses in JSON format"""
        response = web_search_basic(
            "copilot news", subscription_key=self.subscription_key
        )
        try:
            response.json()
        except JSONDecodeError:
            self.fail(
                "Failed to decode response as JSON, check if valid JSON is returned"
            )

    def test_web_search_no_auth(self):
        """Test that Web Search API returns 401 if authorization fails"""
        response = web_search_basic("python crash course", subscription_key="")
        self.assertEqual(response.status_code, 401)

    def test_web_search_response_object_type(self):
        """Test that Web Search API returns the correct type hint"""
        response = web_search_basic(
            "root of pi", subscription_key=self.subscription_key
        )
        try:
            self.assertEqual(response.json()["_type"], "SearchResponse")
        except KeyError:
            self.fail("The response object doesn't include the type hint")

    def test_web_search_response_object_structure(self):
        """Test that Web Search API responses follow the correct structure"""
        response = web_search_basic(
            "fhd license-free wallpaper", subscription_key=self.subscription_key
        )
        response_json = response.json()
        self.assertIn("webPages", response_json)
        self.assertGreater(response_json["webPages"]["totalEstimatedMatches"], 0)
        self.assertGreater(len(response_json["webPages"]["value"]), 0)
        self.assertIn("rankingResponse", response_json)

    @pytest.mark.flaky(retries=5, delay=2)
    def test_web_search_computation(self):
        """Test that Web Search API returns relevant Computation results"""
        response = web_search_basic(
            subscription_key=self.subscription_key, query="289*12 - 492/41"
        )
        self.assertIn("computation", response.json())
        self.assertEqual(3456, int(float(response.json()["computation"]["value"])))


if __name__ == "__main__":
    unittest.main(verbosity=1)
