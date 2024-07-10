# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import os.path
import unittest

try:
    from unittest import mock
except ImportError:
    import mock


from example import run_all_samples


TEST_CONFIG = os.path.join(os.path.dirname(__file__), "testsettings.cfg")


class SearchExampleTest:
    """Simple test launcher for the sample.

    Be sure to set the two environment vaiables before staring it live.
    """

    def test_example(self):
        if self.in_recording:
            run_all_samples()
        else:
            with mock.patch.dict(
                "os.environ",
                {
                    "ENTITYSEARCH_SUBSCRIPTION_KEY": "00000000000000000000000000",
                    "WEBSEARCH_SUBSCRIPTION_KEY": "00000000000000000000000000",
                    "SPELLCHECK_SUBSCRIPTION_KEY": "00000000000000000000000000",
                    "CUSTOMSEARCH_SUBSCRIPTION_KEY": "00000000000000000000000000",
                    "IMAGESEARCH_SUBSCRIPTION_KEY": "00000000000000000000000000",
                    "NEWSSEARCH_SUBSCRIPTION_KEY": "00000000000000000000000000",
                    "WEBSEARCH_SUBSCRIPTION_KEY": "00000000000000000000000000",
                    "CUSTOMVISION_TRAINING_KEY": "00000000000000000000000000",
                    "CUSTOMVISION_PREDICTION_KEY": "00000000000000000000000000",
                },
            ):
                run_all_samples()


if __name__ == "__main__":
    unittest.main()
