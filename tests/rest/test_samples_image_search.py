# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Tests for Image Search REST samples."""

import os
import unittest

import dotenv
from requests import JSONDecodeError

from samples.rest.bing_image_search_v7 import image_search_basic


class ImageSearchRESTSamplesTest(unittest.TestCase):
    """Class for testing REST samples."""

    @classmethod
    def setUpClass(cls):
        cls.dotenv = dotenv.dotenv_values()
        subscription_key_env_var_name = "BING_SEARCH_V7_IMAGE_SEARCH_SUBSCRIPTION_KEY"
        cls.subscription_key = cls.dotenv.get(
            subscription_key_env_var_name, os.environ.get(subscription_key_env_var_name)
        )

    def test_image_search_subscription_key_not_empty(self):
        """Test that the subscription key is defined in the environment"""
        self.assertIsNotNone(self.subscription_key)
        self.assertNotEqual(self.subscription_key, "")

    def test_image_search_basic(self):
        """Test the basic REST call to Image Search API"""
        response = image_search_basic("flowers", subscription_key=self.subscription_key)
        self.assertEqual(response.status_code, 200)

    def test_image_search_response_is_json(self):
        """Test that Image Search API returns responses in JSON format"""
        response = image_search_basic("nature", subscription_key=self.subscription_key)
        try:
            response.json()
        except JSONDecodeError:
            self.fail(
                "Failed to decode response as JSON, check if valid JSON is returned"
            )

    def test_image_search_no_auth(self):
        """Test that Image Search API returns 401 if authorization fails"""
        response = image_search_basic("mountain", subscription_key="")
        self.assertEqual(response.status_code, 401)

    def test_image_search_response_object_type(self):
        """Test that Image Search API returns the correct type hint"""
        response = image_search_basic("river", subscription_key=self.subscription_key)
        try:
            self.assertEqual(response.json()["_type"], "Images")
        except KeyError:
            self.fail("The response object doesn't include the type hint")

    def test_image_search_response_object_structure(self):
        """Test that Image Search API responses follow the correct structure"""
        response = image_search_basic(
            "rainbow ray", subscription_key=self.subscription_key
        )
        response_json = response.json()
        self.assertGreater(response_json["totalEstimatedMatches"], 0)
        try:
            self.assertGreater(len(response_json["value"]), 0)
        except KeyError:
            self.fail("The response object doesn't include any image results")

    def test_image_search_missing_required_parameter(self):
        """Test that Image Search API returns an error with the right structure
        if a required parameter is missing/empty"""
        response = image_search_basic(subscription_key=self.subscription_key, query="")
        # Status Code
        self.assertEqual(response.status_code, 400)
        # Structure
        self.assertIn("_type", response.json())
        self.assertEqual(response.json()["_type"], "ErrorResponse")


if __name__ == "__main__":
    unittest.main(verbosity=1)
