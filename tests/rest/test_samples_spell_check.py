# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Tests for Spell Check REST samples."""

import unittest

import dotenv
from requests import HTTPError, JSONDecodeError

from samples.rest.bing_spell_check_v7 import spell_check_basic


class SpellCheckRESTSamplesTest(unittest.TestCase):
    """Class for testing REST samples."""

    @classmethod
    def setUpClass(cls):
        cls.env = dotenv.dotenv_values()

    def test_spell_check_basic(self):
        """Test the basic REST call to Spell Check API"""
        response = spell_check_basic(
            subscription_key=self.env.get("BING_SEARCH_V7_SPELL_CHECK_SUBSCRIPTION_KEY")
        )
        self.assertEqual(response.status_code, 200)

    def test_spell_check_response_is_json(self):
        """Test that Spell Check API returns responses in JSON format"""
        response = spell_check_basic(
            subscription_key=self.env.get("BING_SEARCH_V7_SPELL_CHECK_SUBSCRIPTION_KEY")
        )
        try:
            response.json()
        except JSONDecodeError:
            self.fail(
                "Failed to decode response as JSON, check if valid JSON is returned"
            )

    def test_spell_check_no_auth(self):
        """Test that Spell Check API returns 401 if authorization fails"""
        with self.assertRaises(Exception) as ex:
            response = spell_check_basic(subscription_key="")
        self.assertEqual(type(ex.exception.__cause__), HTTPError)

    def test_spell_check_response_object_type(self):
        """Test that Spell Check API returns the correct type hint"""
        response = spell_check_basic(
            subscription_key=self.env.get("BING_SEARCH_V7_SPELL_CHECK_SUBSCRIPTION_KEY")
        )
        try:
            self.assertEqual(response.json()["_type"], "SpellCheck")
        except KeyError:
            self.fail("The response object doesn't include the type hint")

    def test_spell_check_response_object_structure(self):
        """Test that Spell Check API responses follow the correct structure"""
        response = spell_check_basic(
            subscription_key=self.env.get("BING_SEARCH_V7_SPELL_CHECK_SUBSCRIPTION_KEY")
        )
        response_json = response.json()
        self.assertIn("flaggedTokens", response_json)

    def test_spell_check_required_parameter_query(self):
        """Test that Entity Search API returns an error if required parameter is empty"""
        with self.assertRaises(Exception) as ex:
            response = spell_check_basic(
                subscription_key=self.env.get(
                    "BING_SEARCH_V7_SPELL_CHECK_SUBSCRIPTION_KEY"
                ),
                query="",
            )
        self.assertEqual(type(ex.exception.__cause__), HTTPError)


if __name__ == "__main__":
    unittest.main(verbosity=1)
