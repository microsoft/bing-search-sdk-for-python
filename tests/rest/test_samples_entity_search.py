# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Tests for Entity Search REST samples."""

import os
import unittest

import dotenv
import pytest
from requests import JSONDecodeError

from samples.rest.bing_entity_search_v7 import entity_search_basic


class EntitySearchRESTSamplesTest(unittest.TestCase):
    """Class for testing REST samples."""

    @classmethod
    def setUpClass(cls):
        cls.dotenv = dotenv.dotenv_values()
        subscription_key_env_var_name = "BING_SEARCH_V7_ENTITY_SEARCH_SUBSCRIPTION_KEY"
        cls.subscription_key = cls.dotenv.get(
            subscription_key_env_var_name, os.environ.get(subscription_key_env_var_name)
        )

    def test_entity_search_subscription_key_not_empty(self):
        """Test that the subscription key is defined in the environment"""
        self.assertIsNotNone(self.subscription_key)
        self.assertNotEqual(self.subscription_key, "")

    def test_entity_search_basic(self):
        """Test the basic REST call to Entity Search API"""
        response = entity_search_basic(
            "alija izetbegović", subscription_key=self.subscription_key
        )
        self.assertEqual(response.status_code, 200)

    def test_entity_search_response_is_json(self):
        """Test that Entity Search API returns responses in JSON format"""
        response = entity_search_basic(
            "Abu Hayyan", subscription_key=self.subscription_key
        )
        try:
            response.json()
        except JSONDecodeError:
            self.fail(
                "Failed to decode response as JSON, check if valid JSON is returned"
            )

    def test_entity_search_no_auth(self):
        """Test that Entity Search API returns 401 if authorization fails"""
        response = entity_search_basic("Egypt", subscription_key="")
        self.assertEqual(response.status_code, 401)

    def test_entity_search_response_object_type(self):
        """Test that Entity Search API returns the correct type hint"""
        response = entity_search_basic(
            "Ghiyath al-Din Muhammad", subscription_key=self.subscription_key
        )
        try:
            self.assertEqual(response.json()["_type"], "SearchResponse")
        except KeyError:
            self.fail("The response object doesn't include the type hint")

    @pytest.mark.flaky(retries=5, delay=2)
    def test_entity_search_response_object_structure(self):
        """Test that Entity Search API responses follow the correct structure"""
        response = entity_search_basic("Arab", subscription_key=self.subscription_key)
        response_json = response.json()
        self.assertIn("entities", response_json)
        self.assertIn("rankingResponse", response_json)
        try:
            self.assertGreater(len(response_json["entities"]["value"]), 0)
        except KeyError:
            self.fail("The response object doesn't include any entity results")

    # https://learn.microsoft.com/en-us/bing/search-apis/bing-entity-search/reference/query-parameters
    def test_entity_search_required_parameter_query(self):
        """Test that Entity Search API returns an error if a required parameter is missing"""
        response = entity_search_basic(subscription_key=self.subscription_key, query="")
        self.assertEqual(response.status_code, 400)

    # https://learn.microsoft.com/en-us/bing/search-apis/bing-entity-search/reference/response-objects#errorresponse
    def test_entity_search_error_response_object_structure(self):
        """Test the structure of the Error Response"""
        response = entity_search_basic("", "")
        try:
            self.assertEqual(response.json()["_type"], "ErrorResponse")
        except KeyError:
            self.fail("The response object is not of type 'ErrorResponse'")


if __name__ == "__main__":
    unittest.main(verbosity=1)
