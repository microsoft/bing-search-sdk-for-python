# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Tests for Auto Suggest REST samples."""

import unittest

import dotenv
from requests import HTTPError, JSONDecodeError

from samples.rest.bing_auto_suggest_v7 import auto_suggest_basic


class AutoSuggestRESTSamplesTest(unittest.TestCase):
    """Class for testing REST samples."""

    @classmethod
    def setUpClass(cls):
        cls.env = dotenv.dotenv_values()

    def test_auto_suggest_basic(self):
        """Test the basic REST call to Auto Suggest API"""
        response = auto_suggest_basic(
            "sail",
            subscription_key=self.env.get(
                "BING_SEARCH_V7_AUTO_SUGGEST_SUBSCRIPTION_KEY"
            ),
        )
        self.assertEqual(response.status_code, 200)

    def test_auto_suggest_response_is_json(self):
        """Test that Auto Suggest API returns responses in JSON format"""
        response = auto_suggest_basic(
            "vim",
            subscription_key=self.env.get(
                "BING_SEARCH_V7_AUTO_SUGGEST_SUBSCRIPTION_KEY"
            ),
        )
        try:
            response.json()
        except JSONDecodeError:
            self.fail(
                "Failed to decode response as JSON, check if valid JSON is returned"
            )

    def test_auto_suggest_no_auth(self):
        """Test that Auto Suggest API returns 401 if authorization fails"""
        with self.assertRaises(Exception) as ex:
            response = auto_suggest_basic("power", subscription_key="")
        self.assertEqual(type(ex.exception.__cause__), HTTPError)

    def test_auto_suggest_response_object_type(self):
        """Test that Auto Suggest API returns the correct type hint"""
        response = auto_suggest_basic(
            "cute",
            subscription_key=self.env.get(
                "BING_SEARCH_V7_AUTO_SUGGEST_SUBSCRIPTION_KEY"
            ),
        )
        try:
            self.assertEqual(response.json()["_type"], "Suggestions")
        except KeyError:
            self.fail("The response object doesn't include the type hint")

    def test_auto_suggest_response_object_structure(self):
        """Test that Auto Suggest API responses follow the correct structure"""
        response = auto_suggest_basic(
            "photography",
            subscription_key=self.env.get(
                "BING_SEARCH_V7_AUTO_SUGGEST_SUBSCRIPTION_KEY"
            ),
        )
        response_json = response.json()
        self.assertIn("suggestionGroups", response_json)
        # Non-empty array of suggestions
        self.assertGreater(
            len(response_json["suggestionGroups"][0]["searchSuggestions"]), 0
        )

    def test_auto_suggest_empty_query_trending(self):
        """Test that Auto Suggest API returns trending searches when the query is empty"""
        response = auto_suggest_basic(
            "",
            subscription_key=self.env.get(
                "BING_SEARCH_V7_AUTO_SUGGEST_SUBSCRIPTION_KEY"
            ),
        )
        response_json = response.json()
        self.assertIn("suggestionGroups", response_json)
        # Non-empty array of suggestions
        self.assertGreater(
            len(response_json["suggestionGroups"][0]["searchSuggestions"]), 0
        )


if __name__ == "__main__":
    unittest.main(verbosity=1)
