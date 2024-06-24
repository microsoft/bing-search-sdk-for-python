# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Tests for Entity Search REST samples."""

import unittest

import dotenv
from requests import HTTPError, JSONDecodeError

from samples.rest.bing_entity_search_v7 import entity_search_basic


class EntitySearchRESTSamplesTest(unittest.TestCase):
    """Class for testing REST samples."""

    @classmethod
    def setUpClass(cls):
        cls.env = dotenv.dotenv_values()

    def test_entity_search_basic(self):
        """Test the basic REST call to Entity Search API"""
        response = entity_search_basic(
            subscription_key=self.env.get(
                "BING_SEARCH_V7_ENTITY_SEARCH_SUBSCRIPTION_KEY"
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_entity_search_response_is_json(self):
        """Test that Entity Search API returns responses in JSON format"""
        response = entity_search_basic(
            subscription_key=self.env.get(
                "BING_SEARCH_V7_ENTITY_SEARCH_SUBSCRIPTION_KEY"
            )
        )
        try:
            response.json()
        except JSONDecodeError:
            self.fail(
                "Failed to decode response as JSON, check if valid JSON is returned"
            )

    def test_entity_search_no_auth(self):
        """Test that Entity Search API returns 401 if authorization fails"""
        with self.assertRaises(Exception) as ex:
            response = entity_search_basic(subscription_key="")
        self.assertEqual(type(ex.exception.__cause__), HTTPError)

    def test_entity_search_response_object_type(self):
        """Test that Entity Search API returns the correct type hint"""
        response = entity_search_basic(
            subscription_key=self.env.get(
                "BING_SEARCH_V7_ENTITY_SEARCH_SUBSCRIPTION_KEY"
            )
        )
        try:
            self.assertEqual(response.json()["_type"], "SearchResponse")
        except KeyError:
            self.fail("The response object doesn't include the type hint")

    def test_entity_search_response_object_structure(self):
        """Test that Entity Search API responses follow the correct structure"""
        response = entity_search_basic(
            subscription_key=self.env.get(
                "BING_SEARCH_V7_ENTITY_SEARCH_SUBSCRIPTION_KEY"
            )
        )
        response_json = response.json()
        self.assertIn("entities", response_json)
        self.assertIn("rankingResponse", response_json)
        try:
            self.assertGreater(len(response_json["entities"]["value"]), 0)
        except KeyError:
            self.fail("The response object doesn't include any entity results")

    # def test_entity_search_required_parameter_query(self):
    #     """Test that Entity Search API returns an error if required parameter is empty"""
    #     response = entity_search_basic(subscription_key=self.env.get(
    #         'BING_SEARCH_V7_ENTITY_SEARCH_SUBSCRIPTION_KEY'), query='')
    #     try:
    #         self.assertEqual(response.json()['_type'], 'ErrorResponse')
    #     except KeyError:
    #         self.fail(
    #             'The response object is not of type \'ErrorResponse\' when the query is empty')


if __name__ == "__main__":
    unittest.main(verbosity=1)
