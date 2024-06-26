# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""Tests for News Search REST samples."""

import unittest

import dotenv
from requests import HTTPError, JSONDecodeError

from samples.rest.bing_news_search_v7 import news_search_basic


class NewsSearchRESTSamplesTest(unittest.TestCase):
    """Class for testing REST samples."""

    @classmethod
    def setUpClass(cls):
        cls.env = dotenv.dotenv_values()

    def test_news_search_basic(self):
        """Test the basic REST call to News Search API"""
        response = news_search_basic(
            "microsoft",
            subscription_key=self.env.get(
                "BING_SEARCH_V7_NEWS_SEARCH_SUBSCRIPTION_KEY"
            ),
        )
        self.assertEqual(response.status_code, 200)

    def test_news_search_response_is_json(self):
        """Test that News Search API returns responses in JSON format"""
        response = news_search_basic(
            "ai",
            subscription_key=self.env.get(
                "BING_SEARCH_V7_NEWS_SEARCH_SUBSCRIPTION_KEY"
            ),
        )
        try:
            response.json()
        except JSONDecodeError:
            self.fail(
                "Failed to decode response as JSON, check if valid JSON is returned"
            )

    def test_news_search_no_auth(self):
        """Test that News Search API returns 401 if authorization fails"""
        with self.assertRaises(Exception) as ex:
            response = news_search_basic("copilot", subscription_key="")
        self.assertEqual(type(ex.exception.__cause__), HTTPError)

    def test_news_search_response_object_type(self):
        """Test that News Search API returns the correct type hint"""
        response = news_search_basic(
            "azure",
            subscription_key=self.env.get(
                "BING_SEARCH_V7_NEWS_SEARCH_SUBSCRIPTION_KEY"
            ),
        )
        try:
            self.assertEqual(response.json()["_type"], "News")
        except KeyError:
            self.fail("The response object doesn't include the type hint")

    def test_news_search_response_object_structure(self):
        """Test that News Search API responses follow the correct structure"""
        response = news_search_basic(
            "vim",
            subscription_key=self.env.get(
                "BING_SEARCH_V7_NEWS_SEARCH_SUBSCRIPTION_KEY"
            ),
        )
        response_json = response.json()
        self.assertTrue(response_json["totalEstimatedMatches"] > 0)
        self.assertGreater(len(response_json["value"]), 0)

    def test_news_search_trending_using_empty_query(self):
        """Test that News Search API returns trending stories if the query is empty"""
        response = news_search_basic(
            subscription_key=self.env.get(
                "BING_SEARCH_V7_NEWS_SEARCH_SUBSCRIPTION_KEY"
            ),
            query="",
        )
        self.assertGreater(len(response.json()["value"]), 0)


if __name__ == "__main__":
    unittest.main()
