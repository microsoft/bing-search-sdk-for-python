<!-- Copyright (c) Microsoft Corporation.
 Licensed under the MIT License. -->
---
page_type: sample
languages:
- python
products:
- Bing Apis
description: "These samples will show you how to get up and running using the Python SDKs."
---

# Bing Apis Python SDK Samples

These samples will show you how to get up and running using the Python SDKs. They'll cover a few rudimentary use cases and hopefully express best practices for interacting with the data from these APIs.

## Features

This project framework provides examples for the following services:



### Language

* Using the **Bing Spell Check SDK** [bing-spellcheck](https://pypi.org/project/microsoft-bing-spellcheck/) for the [Bing Spell Check API](https://docs.microsoft.com/en-us/bing/search-apis/bing-spell-check/overview)


### Search

* Using the **Bing Autosuggest SDK** [bing-search-autosuggest](https://pypi.org/project/microsoft-bing-autosuggest/) for the [Autosuggest API](https://docs.microsoft.com/en-us/bing/search-apis/bing-autosuggest/overview)
* Using the **Bing Custom Search SDK** [bing-search-customsearch](https://pypi.org/project/microsoft-bing-customwebsearch/) for the [Custom Search API](https://docs.microsoft.com/en-us/bing/search-apis/bing-custom-search/overview)
* Using the **Bing Custom Image Search SDK** [bing-search-customimagesearch](https://pypi.org/project/microsoft-bing-customimagesearch/) for the [Custom Image Search API](https://docs.microsoft.com/en-us/bing/search-apis/bing-custom-search/overview)
* Using the **Bing Entity Search SDK** [bing-search-entitysearch](https://pypi.org/project/microsoft-bing-entitysearch/) for the [Entity Search API](https://docs.microsoft.com/en-us/bing/search-apis/bing-entity-search/overview)
* Using the **Bing Image Search SDK** [bing-search-imagesearch](https://pypi.org/project/microsoft-bing-imagesearch/) for the [Image Search API](https://docs.microsoft.com/en-us/bing/search-apis/bing-image-search/overview)
* Using the **Bing News Search SDK** [bing-search-newssearch](https://pypi.org/project/microsoft-bing-newssearch/) for the [News Search API](https://docs.microsoft.com/en-us/bing/search-apis/bing-news-search/overview)
* Using the **Bing Video Search SDK** [bing-search-videosearch](https://pypi.org/project/microsoft-bing-videosearch/) for the [Video Search API](https://docs.microsoft.com/en-us/bing/search-apis/bing-video-search/overview)
* Using the **Bing Visual Search SDK** [bing-search-visualsearch](https://pypi.org/project/microsoft-bing-visualsearch/) for the [Visual Search API](https://docs.microsoft.com/en-us/bing/search-apis/bing-visual-search/overview)
* Using the **Bing Web Search SDK** [bing-search-websearch](https://pypi.org/project/microsoft-bing-websearch/) for the [Web Search API](https://docs.microsoft.com/en-us/bing/search-apis/bing-web-search/overview)


We provide several meta-packages to help you install several packages at a time. Please note that meta-packages are only recommended for development purpose. It's recommended in production to always pin specific version of individual packages.

## Getting Started

### Prerequisites

1.  A Bing API key with which to authenticate the SDK's calls. [Create a new bing account, and try Bing Apis for free.](https://aka.ms/bingapisignup)


### Installation

1.  If you don't already have it, [install Python](https://www.python.org/downloads/).

    This sample (and the SDK) is compatible with Python 2.7, 3.3, 3.4, 3.5 and 3.6.

2.  General recommendation for Python development is to use a Virtual Environment.
    For more information, see https://docs.python.org/3/tutorial/venv.html

    Install and initialize the virtual environment with the "venv" module on Python 3 (you must install [virtualenv](https://pypi.python.org/pypi/virtualenv) for Python 2.7):

    ```
    python -m venv mytestenv # Might be "python3" or "py -3.6" depending on your Python installation
    cd mytestenv
    source bin/activate      # Linux shell (Bash, ZSH, etc.) only
    ./scripts/activate       # PowerShell only
    ./scripts/activate.bat   # Windows CMD only
    ```

### Quickstart

1.  Clone the repository.

    ```
    git clone https://github.com/microsoft/bing-search-sdk-for-python.git
    ```

2.  Install the dependencies using pip.

    ```
    cd bing-search-sdk-for-python
    pip install -r requirements.txt
    ```

4.  Set up the environment variable `SPELLCHECK_SUBSCRIPTION_KEY` with your key if you want to execute SpellCheck tests.
3.  Set up the environment variable `AUTOSUGGEST_SUBSCRIPTION_KEY` with your key if you want to execute Autosuggest tests.
3.  Set up the environment variable `CUSTOMSEARCH_SUBSCRIPTION_KEY` with your key if you want to execute CustomSearch tests.
3.  Set up the environment variable `CUSTOMIMAGESEARCH_SUBSCRIPTION_KEY` with your key if you want to execute CustomImageSearch tests.
3.  Set up the environment variable `ENTITYSEARCH_SUBSCRIPTION_KEY` with your key if you want to execute EntitySearch tests.
4.  Set up the environment variable `IMAGESEARCH_SUBSCRIPTION_KEY` with your key if you want to execute ImageSearch tests.
4.  Set up the environment variable `NEWSSEARCH_SUBSCRIPTION_KEY` with your key if you want to execute NewsSearch tests.
4.  Set up the environment variable `VIDEOSEARCH_SUBSCRIPTION_KEY` with your key if you want to execute VideoSearch tests.
4.  Set up the environment variable `VISUALSEARCH_SUBSCRIPTION_KEY` with your key if you want to execute VideoSearch tests.
4.  Set up the environment variable `WEBSEARCH_SUBSCRIPTION_KEY` with your key if you want to execute WebSearch tests.



## Demo

A demo app is included to show how to use the project.

To run the complete demo, execute `python example.py`

To run each individual demo, point directly to the file. For example (i.e. not complete list):

1. `python samples/sdk/spellcheck_samples.py`
2. `python samples/sdk/entity_search_samples.py`
3. `python samples/sdk/video_search_samples.py`

To see the code of each example, simply look at the examples in the Samples folder. They are written to be isolated in scope so that you can see only what you're interested in.

## Resources

- https://github.com/microsoft/bing-search-sdk-for-python
