# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Tests for News Search REST samples."""

import os
import unittest

import dotenv
import pytest
from requests import JSONDecodeError

from samples.rest.bing_news_search_v7 import news_search_basic


class NewsSearchRESTSamplesTest(unittest.TestCase):
    """Class for testing REST samples."""

    @classmethod
    def setUpClass(cls):
        cls.dotenv = dotenv.dotenv_values()
        subscription_key_env_var_name = "BING_SEARCH_V7_NEWS_SEARCH_SUBSCRIPTION_KEY"
        cls.subscription_key = cls.dotenv.get(
            subscription_key_env_var_name, os.environ.get(subscription_key_env_var_name)
        )

    def test_news_search_subscription_key_not_empty(self):
        """Test that the subscription key is defined in the environment"""
        self.assertIsNotNone(self.subscription_key)
        self.assertNotEqual(self.subscription_key, "")

    def test_news_search_basic(self):
        """Test the basic REST call to News Search API"""
        response = news_search_basic(
            "microsoft", subscription_key=self.subscription_key
        )
        self.assertEqual(response.status_code, 200)

    def test_news_search_response_is_json(self):
        """Test that News Search API returns responses in JSON format"""
        response = news_search_basic("ai", subscription_key=self.subscription_key)
        try:
            response.json()
        except JSONDecodeError:
            self.fail(
                "Failed to decode response as JSON, check if valid JSON is returned"
            )

    def test_news_search_no_auth(self):
        """Test that News Search API returns 401 if authorization fails"""
        response = news_search_basic("copilot", subscription_key="")
        self.assertEqual(response.status_code, 401)

    def test_news_search_response_object_type(self):
        """Test that News Search API returns the correct type hint"""
        response = news_search_basic("azure", subscription_key=self.subscription_key)
        try:
            self.assertEqual(response.json()["_type"], "News")
        except KeyError:
            self.fail("The response object doesn't include the type hint")

    def test_news_search_response_object_structure(self):
        """Test that News Search API responses follow the correct structure"""
        response = news_search_basic("vim", subscription_key=self.subscription_key)
        response_json = response.json()
        self.assertTrue(response_json["totalEstimatedMatches"] > 0)
        self.assertGreater(len(response_json["value"]), 0)

    @pytest.mark.xfail(
        reason="issue in the api itself, see:\n\
        https://learn.microsoft.com/en-us/bing/search-apis/bing-news-search/reference/query-parameters"
    )
    def test_news_search_trending_using_empty_query(self):
        """Test that News Search API returns trending stories if the query is empty"""
        response = news_search_basic(query="", subscription_key=self.subscription_key)
        self.assertTrue(response.ok)
        try:
            self.assertGreater(len(response.json()["value"]), 0)
        except JSONDecodeError:
            self.fail("The response is not JSON")
        except (KeyError, TypeError):
            self.fail("The response doesn't have the correct structure")


if __name__ == "__main__":
    unittest.main()
