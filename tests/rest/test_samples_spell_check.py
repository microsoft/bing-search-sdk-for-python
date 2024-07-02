# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Tests for Spell Check REST samples."""

import os
import unittest

import dotenv
from requests import JSONDecodeError

from samples.rest.bing_spell_check_v7 import spell_check_basic


class SpellCheckRESTSamplesTest(unittest.TestCase):
    """Class for testing REST samples."""

    @classmethod
    def setUpClass(cls):
        cls.dotenv = dotenv.dotenv_values()
        subscription_key_env_var_name = "BING_SEARCH_V7_SPELL_CHECK_SUBSCRIPTION_KEY"
        cls.subscription_key = cls.dotenv.get(
            subscription_key_env_var_name, os.environ.get(subscription_key_env_var_name)
        )

    def test_spell_check_subscription_key_not_empty(self):
        """Test that the subscription key is defined in the environment"""
        self.assertIsNotNone(self.subscription_key)
        self.assertNotEqual(self.subscription_key, "")

    def test_spell_check_basic(self):
        """Test the basic REST call to Spell Check API"""
        response = spell_check_basic(
            "helo wordl", subscription_key=self.subscription_key
        )
        self.assertEqual(response.status_code, 200)

    def test_spell_check_response_is_json(self):
        """Test that Spell Check API returns responses in JSON format"""
        response = spell_check_basic(
            "mine pizza", subscription_key=self.subscription_key
        )
        try:
            response.json()
        except JSONDecodeError:
            self.fail(
                "Failed to decode response as JSON, check if valid JSON is returned"
            )

    def test_spell_check_no_auth(self):
        """Test that Spell Check API returns 401 if authorization fails"""
        response = spell_check_basic("give me this this", subscription_key="")
        self.assertEqual(response.status_code, 401)

    def test_spell_check_response_object_type(self):
        """Test that Spell Check API returns the correct type hint"""
        response = spell_check_basic(
            "best top laptop", subscription_key=self.subscription_key
        )
        try:
            self.assertEqual(response.json()["_type"], "SpellCheck")
        except KeyError:
            self.fail("The response object doesn't include the type hint")

    def test_spell_check_response_object_structure(self):
        """Test that Spell Check API responses follow the correct structure"""
        response = spell_check_basic(
            "widnows lapyop", subscription_key=self.subscription_key
        )
        response_json = response.json()
        self.assertIn("flaggedTokens", response_json)

    def test_spell_check_required_parameter_query(self):
        """Test that Spell Check API returns an error if a required parameter is missing"""
        response = spell_check_basic(query="", subscription_key=self.subscription_key)
        self.assertEqual(response.status_code, 400)

    # https://learn.microsoft.com/en-us/bing/search-apis/bing-spell-check/reference/response-objects#errorresponse
    def test_spell_check_error_response_object_structure(self):
        """Test the structure of the Error Response"""
        response = spell_check_basic("", "")
        try:
            self.assertEqual(response.json()["_type"], "ErrorResponse")
        except KeyError:
            self.fail("The response object type hint is missing")


if __name__ == "__main__":
    unittest.main(verbosity=1)
