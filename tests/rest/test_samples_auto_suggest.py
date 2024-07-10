# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Tests for Auto Suggest REST samples."""

import os
import unittest

import dotenv
import pytest
from requests import JSONDecodeError

from samples.rest.bing_auto_suggest_v7 import auto_suggest_basic


class AutoSuggestRESTSamplesTest(unittest.TestCase):
    """Class for testing REST samples."""

    @classmethod
    def setUpClass(cls):
        cls.dotenv = dotenv.dotenv_values()
        subscription_key_env_var_name = "BING_SEARCH_V7_AUTO_SUGGEST_SUBSCRIPTION_KEY"
        cls.subscription_key = cls.dotenv.get(
            subscription_key_env_var_name, os.environ.get(subscription_key_env_var_name)
        )

    def test_auto_suggest_subscription_key_not_empty(self):
        """Test that the subscription key is defined in the environment"""
        self.assertIsNotNone(self.subscription_key)
        self.assertNotEqual(self.subscription_key, "")

    def test_auto_suggest_basic(self):
        """Test the basic REST call to Auto Suggest API"""
        response = auto_suggest_basic("sail", subscription_key=self.subscription_key)
        self.assertEqual(response.status_code, 200)

    def test_auto_suggest_response_is_json(self):
        """Test that Auto Suggest API returns responses in JSON format"""
        response = auto_suggest_basic("vim", subscription_key=self.subscription_key)
        try:
            response.json()
        except JSONDecodeError:
            self.fail(
                "Failed to decode response as JSON, check if valid JSON is returned"
            )

    def test_auto_suggest_no_auth(self):
        """Test that Auto Suggest API returns 401 if authorization fails"""
        response = auto_suggest_basic("power", subscription_key="")
        self.assertEqual(response.status_code, 401)

    def test_auto_suggest_response_object_type(self):
        """Test that Auto Suggest API returns the correct type hint"""
        response = auto_suggest_basic("cute", subscription_key=self.subscription_key)
        try:
            self.assertEqual(response.json()["_type"], "Suggestions")
        except KeyError:
            self.fail("The response object doesn't include the type hint")

    def test_auto_suggest_response_object_structure(self):
        """Test that Auto Suggest API responses follow the correct structure"""
        response = auto_suggest_basic(
            "photography", subscription_key=self.subscription_key
        )
        response_json = response.json()
        self.assertIn("suggestionGroups", response_json)
        # Non-empty array of suggestions
        self.assertGreater(
            len(response_json["suggestionGroups"][0]["searchSuggestions"]), 0
        )

    @pytest.mark.xfail(
        reason="issue in the api itself, see:\n\
        https://learn.microsoft.com/en-us/bing/search-apis/bing-autosuggest/reference/response-objects#errorresponse"
    )
    def test_auto_suggest_error_response_object_structure(self):
        """Test the structure of the Error Response"""
        response = auto_suggest_basic("", subscription_key="")
        try:
            self.assertEqual(response.json()["_type"], "ErrorResponse")
        except KeyError:
            self.fail("The response object type hint is missing")

    def test_auto_suggest_empty_query_trending(self):
        """Test that Auto Suggest API returns trending searches when the query is empty"""
        response = auto_suggest_basic("", subscription_key=self.subscription_key)
        response_json = response.json()
        self.assertIn("suggestionGroups", response_json)
        # Non-empty array of suggestions
        self.assertGreater(
            len(response_json["suggestionGroups"][0]["searchSuggestions"]), 0
        )


if __name__ == "__main__":
    unittest.main(verbosity=1)
