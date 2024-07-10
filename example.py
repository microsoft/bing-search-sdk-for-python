"""Sample launcher.

This file is just the samples launcher. Nothing here os related
to Bing Apis. Look into the "samples" folder for actual code
"""

import importlib
import pkgutil

# import logging
# logging.basicConfig(level=logging.DEBUG)

import tools
import os, sys, inspect
import samples.sdk


def run_all_samples():
    for _, section_name_name, ispkg in pkgutil.walk_packages(samples.sdk.__path__):
        section_package_name = "samples.sdk." + section_name_name
        section_package = importlib.import_module(section_package_name)
        sample_module = importlib.import_module(section_package_name)
        subkey_env_name = getattr(sample_module, "SUBSCRIPTION_KEY", None)
        if not subkey_env_name:
            continue
        print("Executing sample from ", section_name_name)
        try:
            tools.execute_samples(sample_module.__dict__, subkey_env_name)
        except tools.SubscriptionKeyError as err:
            print("{}\n".format(err))


if __name__ == "__main__":
    run_all_samples()
