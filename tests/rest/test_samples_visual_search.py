# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Tests for Visual Search REST samples."""

import unittest

import dotenv
from requests import JSONDecodeError

from samples.rest.bing_visual_search_v7 import visual_search_basic


class VisualSearchRESTSamplesTest(unittest.TestCase):
    """Class for testing REST samples."""

    @classmethod
    def setUpClass(cls):
        cls.env = dotenv.dotenv_values()
        cls.subscription_key = cls.env.get(
            "BING_SEARCH_V7_VISUAL_SEARCH_SUBSCRIPTION_KEY"
        )

    def test_visual_search_subscription_key_not_empty(self):
        """Test that the subscription key is defined in the environment"""
        self.assertIsNotNone(self.subscription_key)
        self.assertNotEqual(self.subscription_key, "")

    def test_visual_search_basic(self):
        """Test the basic REST call to Visual Search API"""
        response = visual_search_basic(subscription_key=self.subscription_key)
        self.assertEqual(response.status_code, 200)

    def test_visual_search_response_is_json(self):
        """Test that Visual Search API returns responses in JSON format"""
        response = visual_search_basic(subscription_key=self.subscription_key)
        try:
            response.json()
        except JSONDecodeError:
            self.fail(
                "Failed to decode response as JSON, check if valid JSON is returned"
            )

    def test_visual_search_no_auth(self):
        """Test that Visual Search API returns 401 if authorization fails"""
        response = visual_search_basic(subscription_key="")
        self.assertEqual(response.status_code, 401)

    def test_visual_search_response_object_type(self):
        """Test that Visual Search API returns the correct type hint"""
        response = visual_search_basic(subscription_key=self.subscription_key)
        try:
            self.assertEqual(response.json()["_type"], "ImageKnowledge")
        except KeyError:
            self.fail("The response object doesn't include the type hint")

    def test_visual_search_response_object_structure(self):
        """Test that Visual Search API responses follow the correct structure"""
        response = visual_search_basic(subscription_key=self.subscription_key)
        response_json = response.json()
        self.assertIn("image", response_json)
        self.assertIn("imageInsightsToken", response_json["image"])
        try:
            self.assertGreater(len(response_json["tags"]), 0)
        except KeyError:
            self.fail("The response object doesn't include any visual results")


if __name__ == "__main__":
    unittest.main(verbosity=1)
